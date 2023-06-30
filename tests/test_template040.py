from pathlib import Path

import pytest
from rdflib import Graph, Literal, URIRef, compare
from rdflib.namespace import SKOS
from vocexcel import convert
from vocexcel.utils import ConversionError


def test_simple():
    convert.excel_to_rdf(
        Path(__file__).parent / "040_simple_valid.xlsx", output_type="file"
    )
    g = Graph().parse(Path(__file__).parent / "040_simple_valid.ttl")
    assert len(g) == 142
    assert (
        URIRef(
            "http://resource.geosciml.org/classifierscheme/cgi/2016.01/particletype"
        ),
        SKOS.prefLabel,
        Literal("Particle Type", lang="en"),
    ) in g, "PrefLabel for vocab is not correct"
    # tidy up
    Path(Path(__file__).parent / "040_simple_valid.ttl").unlink()


def test_complex():
    convert.excel_to_rdf(
        Path(__file__).parent / "040_complex_valid.xlsx", output_type="file"
    )
    g = Graph().parse(Path(__file__).parent / "040_complex_valid.ttl")
    assert len(g) == 142
    assert (
        URIRef(
            "http://resource.geosciml.org/classifierscheme/cgi/2016.01/particletype"
        ),
        SKOS.prefLabel,
        Literal("Particle Type", lang="en"),
    ) in g, "PrefLabel for vocab is not correct"
    # tidy up
    Path(Path(__file__).parent / "040_complex_valid.ttl").unlink()


def test_empty_template():
    assert Path(
        Path(__file__).parent.parent / "templates" / "VocExcel-template_040.xlsx"
    ).is_file()
    with pytest.raises(ConversionError) as e:
        convert.excel_to_rdf(
            Path(__file__).parent.parent / "templates" / "VocExcel-template_040.xlsx",
            output_type="file",
        )
    assert "7 validation errors for ConceptScheme" in str(e)


# isomorphic tests
def test_exhaustive_template_is_isomorphic():
    g1 = Graph().parse(
        Path(__file__).parent / "040_exhaustive_example_perfect_output.ttl"
    )
    g2 = convert.excel_to_rdf(
        Path(__file__).parent / "040_exhaustive_example.xlsx", output_type="graph"
    )
    assert compare.isomorphic(g1, g2), "Graphs are not Isomorphic"


def test_minimal_template_is_isomorphic():
    g1 = Graph().parse(Path(__file__).parent / "040_minimal_example_perfect_output.ttl")
    g2 = convert.excel_to_rdf(
        Path(__file__).parent / "040_minimal_example.xlsx", output_type="graph"
    )
    assert compare.isomorphic(g1, g2), "Graphs are not Isomorphic"
