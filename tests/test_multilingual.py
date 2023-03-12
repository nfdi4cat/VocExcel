import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.absolute()))
from pathlib import Path

from rdflib import Graph
from vocexcel import convert


def test_countrycodes():
    convert.excel_to_rdf(Path(__file__).parent / "030_eg-languages-valid.xlsx")

    # file eg-languages-valid.ttl should have been created
    g = Graph().parse(Path(__file__).parent / "030_eg-languages-valid.ttl")
    assert len(g) == 4940

    # clean up
    Path.unlink(Path(__file__).parent / "030_eg-languages-valid.ttl", missing_ok=True)


if __name__ == "__main__":
    print(test_countrycodes())
