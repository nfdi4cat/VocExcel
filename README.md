**This fork is archived!** (2023-07-05) - Some parts/files of this repository were [merged](https://github.com/nfdi4cat/voc4cat-tool/pull/119) into [NFDI4Cat/voc4cat-tool](https://github.com/nfdi4cat/voc4cat-tool) including their git-history.

# VocExcel

> *This is a fork! The original project (now at [RDFlib/vocexcel](https://github.com/RDFLib/VocExcel)) changed its templates substantially
> which made it too cumbersome to keep our code and the customized templates compatible.*

VocExcel is another Excel to RDF converter for SKOS vocabs, but one that uses fixed template to achieve particular SKOS profile outcomes!

## How to use

### Creating vocabularies

The template files in this repository's *templates/* folder are to be used to create vocabularies. The templates contains all the basics needed to understand what to do including notes, examples and so on. Vocab authors only need this template file to create vocabulary content.

*Note: example sheets for various template versions are in the tests folder. Just ensure you're looking at examples prefixed with the template version you are after. Both simple and complex vocabularies are exemplified.*

There are multiple versions of template in the *templates/* folder. You are free to use any of them however the latest is usually the greatest!

Use one Excel workbook per vocabulary.

### Installation

Several forms of use of this tool do not require any installation - see the next section. However, to run the tool as a Python script or a module, you will need to:

1. have Python (3.8+) installed on your computer
2. create a poetry environment
3. install the necessary packages in that environment
   : - when running a poetry environment, some IDE's like python will automatically install the pyproject.toml else, there would have to be a manual install with something like 'poetry install'
4. run the script, `convert.py`, using the version of Python in your poetry environment

### Generating RDF from Excel

There are several methods available to process vocabularies entered into the Excel template using resources in this repository:

1. Windows command line
2. Shell command line script (Linux/Unix/Mac)
3. Python script
4. Python module
5. *voc4cat-enabled github-repos*

Methods 1 & 2 all use the same options. See the section [Command Line Arguments].

#### 1. Windows command line

After installation an executable file, `vocexcel.exe`, is available in the `vocexcel/bin/` folder. It can be used like this:

```cmd
c:\Users\user> vocexcel.exe vocabulary-x.xlsx
```

This command will generate either a vocabulary RDF file in the same directory as the input Excel file, or an Excel file from the RDF file, based on file endings.

#### 2. Shell command line script (Linux/Unix/Mac)

The script `vocexcel/bin/vocexcel.sh` can be run as a shell script on Linux/Unix/Mac with the same options as the Windows EXE program.

```bash
~$ sh vocexcel.sh vocabulary-x.xlsx
```

Note that to run this shell script, you need to have installed a Python environment that contains this program's dependencies which are all listed in `requirements.txt`. The shell script then needs to be told where the Python environment is: see the `PYTHON` variable in the script.

The script will work out, based on file endings, if this is an Excel to RDF or an RDF to Excel conversion.

#### 3. Python script

The Python script `convert.py` in the `vocexcel/` directory can be run on Windows/Unix/Linux/Mac systems like this:

```bash
~$ python convert.py vocabulary-x.xlsx
```

As long as a Python environment containing the program's needed modules, listed in `requirements.txt` are installed. As above, the script will work out, based on file endings, if this is an Excel to RDF or an RDF to Excel conversion.

#### 4. Python module

The converter program has two methods that can be called from other Python programs, perhaps as part of a chain of processing, for Excel to RDF and RDF to Excel: `rdf_to_excel()` & `excel_to_rdf()`. For this, you would need code like this:

```python
from vocexcel import convert
from pathlib import Path

convert.rdf_to_excel(Path(".") / "path" / "to" / "vocab-file.xlsx")
```

Or similar code for the reverse conversion, RDF to Excel using `convert.excel_to_rdf()`.

This will create an output file, `vocab-file.ttl` for Excel to RDF, in the same directory as the input file.

There are several options for the conversion functions, just see the functions themselves in `vocexcel/convert.py`.

#### 5. voc4cat-enabled github repos

*More info coming soon!*.

#### Command Line Arguments

All command line options can be printed out by the Windows, Linux/Unix/Mac versions of the tools by specifying `-h` for 'help' like this:

```bash
> vocexcel.exe -h

~$ sh vocexcel.sh -h
```

This will print something like the following:

```text
usage: vocexcel [-h] [-v] [--listprofiles] [--validate] [-p PROFILE]
                [--outputtype {file,string}] [-o OUTPUTFILE]
                [--outputformat {turtle,xml,json-ld}] [-s SHEET] [-t TEMPLATEFILE]
                [-e ERRORLEVEL] [-m MESSAGELEVEL] [-l LOGFILE]
                [file_to_convert]

positional arguments:
  file_to_convert       The Excel file to convert to a SKOS vocabulary in RDF
                        or an RDF file to convert to an Excel file (default: None)

options:
  -h, --help            show this help message and exit
  -v, --version         The version of this copy of VocExcel. (default: False)
  --listprofiles        This flag, if set, must be the only flag supplied. It will cause the
                        program to list all the vocabulary profiles that this converter,
                        indicating both their URI and their short token for use with
                        the -p (--profile) flag when converting Excel files (default: False)
  --validate            Validate output file (default: False)
  -p PROFILE, --profile PROFILE
                        A profile - a specified information model - for a vocabulary. This tool
                        understands several profiles and you can choose which one you want to
                        convert the Excel file according to. The list of profiles - URIs and
                        their corresponding tokens - supported by VocExcel, can be found
                        by running the program with the flag -lp or --listprofiles.
                        (default: vocpub)
  --outputtype {file,string}
                        The format of the vocabulary output. (default: file)
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        An optionally-provided output file path. (default: None)
  --outputformat {turtle,xml,json-ld}
                        An optionally-provided output format for RDF files. Only relevant
                        in Excel-to-RDf conversions. (default: turtle)
  -s SHEET, --sheet SHEET
                        The sheet within the target Excel Workbook to process.
                        (default: vocabulary)
  -t TEMPLATEFILE, --templatefile TEMPLATEFILE
                        An optionally-provided Excel-template file to be used in
                        SKOS-> Excel conversion. (default: None)
  -e ERRORLEVEL, --errorlevel ERRORLEVEL
                        The minimum severity level which fails validation (default: 1)
  -m MESSAGELEVEL, --messagelevel MESSAGELEVEL
                        The minimum severity level printed to console (default: 1)
  -l LOGFILE, --logfile LOGFILE
                        The file to write logging output to (default: None)
```

## License

This code is licensed under the BSD-3-Clause license. See the [LICENSE
file](LICENSE) for the deed.

Note that Excel is trademark/property of Microsoft.
