import nbformat as nbf
import argparse
import glob
import os
import shutil



def filter_colab_cells(nb_path):
    shutil.copy(nb_path, nb_path + ".bak")
    nb = nbf.read(nb_path, as_version=nbf.NO_CONVERT)

    new_cells = []
    for cell in nb.cells:
        include = True
        for line in cell.source.split("\n"):
            if line.strip().startswith("!"):
                include = False
                break
        if include:
            new_cells.append(cell)
    
    nb.cells = new_cells
    nbf.write(nb, nb_path)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("submission_path", type=str)

    args = argparser.parse_args()

    colab_nb = glob.glob(os.path.join(args.submission_path, "*.ipynb"))
    if len(colab_nb) < 1:
        for nb_path in glob.glob(os.path.join(args.submission_path, "*")):
            shutil.move(nb_path, f"{nb_path}.ipynb")
            break

    for nb_path in glob.glob(os.path.join(args.submission_path, "*.ipynb")):
        filter_colab_cells(nb_path)


if __name__ == "__main__":
    main()
