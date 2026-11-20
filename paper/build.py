"""Build the manuscript and reject final warnings or box defects."""
from pathlib import Path
import argparse
import os
import re
import shutil
import subprocess


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", default=".build")
    parser.add_argument("--engine", default="pdflatex")
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    build = Path(args.build_dir).resolve()
    build.mkdir(parents=True, exist_ok=True)
    engine = shutil.which(args.engine)
    if not engine:
        raise SystemExit("pdfLaTeX is required; install it separately before building.")
    command = [engine, "--disable-installer", "-no-shell-escape", "-halt-on-error",
               "-interaction=nonstopmode", "-file-line-error",
               "-output-directory=" + str(build), "main.tex"]
    environment = os.environ.copy()
    environment["MIKTEX_ENABLE_INSTALLER"] = "0"
    previous = None
    stable = False
    for iteration in range(6):
        result = subprocess.run(command, cwd=source, env=environment,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (build / "engine.txt").write_bytes(result.stdout)
        if result.returncode:
            print(result.stdout.decode("utf-8", errors="replace"))
            raise SystemExit("pdfLaTeX failed; automatic package installation is disabled.")
        state = tuple((build / ("main." + ext)).read_bytes()
                      if (build / ("main." + ext)).exists() else b""
                      for ext in ("aux", "toc", "out"))
        if state == previous:
            stable = True
            break
        previous = state
    if not stable:
        raise SystemExit("Cross-reference files did not stabilize in six passes.")
    log = (build / "main.log").read_text(encoding="utf-8", errors="replace")
    bad = re.findall(r"(?im)^.*(?:LaTeX(?: Font)? Warning:|Package [^ ]+ Warning:|Class [^ ]+ Warning:|pdfTeX warning|overfull|underfull|undefined references|undefined citations|missing character:|^!).*$", log)
    if bad:
        print("\n".join(bad))
        raise SystemExit("Strict build failed: final warnings or box defects.")
    shutil.copyfile(build / "main.pdf", source / "main.pdf")
    print("CLEAN: references stable; zero warnings and zero box defects.")


if __name__ == "__main__":
    main()
