from typing import List, Tuple

from openpyxl.worksheet.worksheet import Worksheet
from pydantic import ValidationError

try:
    import models
    from utils import ConversionError, split_and_tidy
except:
    import sys

    sys.path.append("..")
    from vocexcel import models
    from vocexcel.utils import ConversionError, split_and_tidy


def extract_concepts_and_collections(
    s: Worksheet,
) -> Tuple[List[models.Concept], List[models.Collection]]:
    concepts = []
    collections = []
    process_concept = False
    process_collection = False
    for col in s.iter_cols(max_col=1):
        for cell in col:
            row = cell.row
            if cell.value == "Concept URI":
                process_concept = True
            elif cell.value == "Collection URI":
                process_concept = False
                process_collection = True
            elif process_concept:
                if cell.value is None:
                    pass
                else:
                    try:
                        c = models.Concept(
                            uri=s[f"A{row}"].value,
                            pref_label=s[f"B{row}"].value,
                            alt_labels=split_and_tidy(s[f"C{row}"].value),
                            pl_language_code=split_and_tidy(s[f"D{row}"].value),
                            definition=s[f"E{row}"].value,
                            children=split_and_tidy(s[f"F{row}"].value),
                            other_ids=split_and_tidy(s[f"G{row}"].value),
                            home_vocab_uri=s[f"H{row}"].value,
                            provenance=s[f"I{row}"].value,
                        )

                        concepts.append(c)
                    except ValidationError as e:
                        raise ConversionError(
                            f"Concept processing error potentially at row {row}, with error: {e}"
                        )
            elif process_collection:
                if cell.value is None:
                    pass
                else:
                    try:
                        c = models.Collection(
                            uri=s[f"A{row}"].value,
                            pref_label=s[f"B{row}"].value,
                            definition=s[f"C{row}"].value,
                            members=split_and_tidy(s[f"D{row}"].value),
                            provenance=s[f"E{row}"].value,
                        )
                        collections.append(c)
                    except ValidationError as e:
                        raise ConversionError(
                            f"Collection processing error, row {row}, error: {e}"
                        )
            elif cell.value is None:
                pass

    return concepts, collections
