# coding=utf-8
# Copyright 2022 HuggingFace Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""TODO"""

from datetime import datetime
from typing import Optional
import datasets
import re


_CITATION = """\
TODO
"""

_DESCRIPTION = """\
TODO
"""
_BASE_URL_TRAIN_DEV_TEST = "https://raw.githubusercontent.com/hipe-eval/HIPE-2022-data/main/data/v2.1/hipe2020/"


_URLs = {
    "EN": {
        "dev": _BASE_URL_TRAIN_DEV_TEST + "en/HIPE-2022-v2.1-hipe2020-dev-en.tsv",
        "test": _BASE_URL_TRAIN_DEV_TEST + "en/HIPE-2022-v2.1-hipe2020-test_allmasked-en.tsv"
    },  # English only no train
    "DE": {
        "dev": _BASE_URL_TRAIN_DEV_TEST + "de/HIPE-2022-v2.1-hipe2020-dev-de.tsv",
        "train": _BASE_URL_TRAIN_DEV_TEST + "de/HIPE-2022-v2.1-hipe2020-train-de.tsv",
        "test": _BASE_URL_TRAIN_DEV_TEST + "de/HIPE-2022-v2.1-hipe2020-test_allmasked-de.tsv"
    },
    "FR": {
        "dev": _BASE_URL_TRAIN_DEV_TEST + "fr/HIPE-2022-v2.1-hipe2020-dev-fr.tsv",
        "train": _BASE_URL_TRAIN_DEV_TEST + "fr/HIPE-2022-v2.1-hipe2020-train-fr.tsv",
        "test": _BASE_URL_TRAIN_DEV_TEST + "fr/HIPE-2022-v2.1-hipe2020-test_allmasked-fr.tsv"
    },
}




class HIPE2020Config(datasets.BuilderConfig):
    """BuilderConfig for HIPE2020"""

    def __init__(self, data_urls,**kwargs):
        """BuilderConfig for HIPE2020.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(HIPE2020Config, self).__init__(**kwargs)
        self.data_urls = data_urls


class HIPE2020(datasets.GeneratorBasedBuilder):
    """HIPE2020 dataset."""

    BUILDER_CONFIGS = [
        HIPE2020Config(
            name="en",
            data_urls=_URLs["EN"],
            version=datasets.Version("1.0.0"),
            description="HIPE dataset covering English",
        ),
        HIPE2020Config(
            name="de",
            data_urls=_URLs["DE"],
            version=datasets.Version("1.0.0"),
            description="HIPE dataset covering German",
        ),
        HIPE2020Config(
            name="fr",
            data_urls=_URLs["FR"],
            version=datasets.Version("1.0.0"),
            description="HIPE dataset covering French",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "NE_COARSE_LIT": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-comp",
                                "B-loc",
                                "B-org",
                                "B-pers",
                                "B-prod",
                                "B-time",
                                "I-loc",
                                "I-org",
                                "I-pers",
                                "I-prod",
                                "I-time",
                                "_",
                            ]
                        )
                    ),
                    "NE_COARSE_METO_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-loc",
                                "B-org",
                                "B-pers",
                                "B-prod",
                                "B-time",
                                "I-loc",
                                "I-org",
                                "I-pers",
                                "_",
                            ]
                        )
                    ),
                    "NE_FINE_LIT_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-comp.name",
                                "B-loc",
                                "B-loc.add.elec",
                                "B-loc.add.phys",
                                "B-loc.adm.nat",
                                "B-loc.adm.reg",
                                "B-loc.adm.sup",
                                "B-loc.adm.town",
                                "B-loc.fac",
                                "B-loc.oro",
                                "B-loc.phys.astro",
                                "B-loc.phys.geo",
                                "B-loc.phys.hydro",
                                "B-loc.unk",
                                "B-org",
                                "B-org.adm",
                                "B-org.ent",
                                "B-org.ent.pressagency",
                                "B-pers",
                                "B-pers.coll",
                                "B-pers.ind",
                                "B-pers.ind.articleauthor",
                                "B-prod",
                                "B-prod.doctr",
                                "B-prod.media",
                                "B-time",
                                "B-time.date.abs",
                                "I-loc",
                                "I-loc.add.elec",
                                "I-loc.add.phys",
                                "I-loc.adm.nat",
                                "I-loc.adm.reg",
                                "I-loc.adm.sup",
                                "I-loc.adm.town",
                                "I-loc.fac",
                                "I-loc.oro",
                                "I-loc.phys.astro",
                                "I-loc.phys.geo",
                                "I-loc.phys.hydro",
                                "I-loc.unk",
                                "I-org",
                                "I-org.adm",
                                "I-org.ent",
                                "I-org.ent.pressagency",
                                "I-pers",
                                "I-pers.coll",
                                "I-pers.ind",
                                "I-pers.ind.articleauthor",
                                "I-prod",
                                "I-prod.doctr",
                                "I-prod.media",
                                "I-time",
                                "I-time.date.abs",
                                "_",
                            ]
                        )
                    ),
                    "NE_FINE_METO_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-loc",
                                "B-loc.adm.nat",
                                "B-loc.adm.reg",
                                "B-loc.adm.town",
                                "B-loc.fac",
                                "B-loc.oro",
                                "B-org",
                                "B-org.adm",
                                "B-org.ent",
                                "B-pers.coll",
                                "B-pers.ind",
                                "B-prod.media",
                                "B-time.date.abs",
                                "I-loc",
                                "I-loc.adm.nat",
                                "I-loc.adm.reg",
                                "I-loc.fac",
                                "I-loc.oro",
                                "I-org",
                                "I-org.adm",
                                "I-org.ent",
                                "I-pers",
                                "I-pers.ind",
                                "_",
                            ]
                        )
                    ),
                    "NE_FINE_COMP_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-comp.demonym",
                                "B-comp.function",
                                "B-comp.name",
                                "B-comp.qualifier",
                                "B-comp.title",
                                "I-comp.demonym",
                                "I-comp.function",
                                "I-comp.name",
                                "I-comp.qualifier",
                                "I-comp.title",
                                "_",
                            ]
                        )
                    ),
                    "NE_NESTED_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-loc",
                                "B-loc.adm.nat",
                                "B-loc.adm.reg",
                                "B-loc.adm.sup",
                                "B-loc.adm.town",
                                "B-loc.fac",
                                "B-loc.oro",
                                "B-loc.phys.geo",
                                "B-loc.phys.hydro",
                                "B-org",
                                "B-org.adm",
                                "B-org.ent",
                                "B-pers.coll",
                                "B-pers.ind",
                                "B-prod.media",
                                "B-time.date.abs",
                                "I-loc",
                                "I-loc.adm.nat",
                                "I-loc.adm.reg",
                                "I-loc.adm.town",
                                "I-loc.adm.sup",
                                "I-loc.fac",
                                "I-loc.oro",
                                "I-loc.phys.astro",
                                "I-loc.phys.geo",
                                "I-loc.phys.hydro",
                                "I-org",
                                "I-org.adm",
                                "I-org.ent",
                                "I-pers.ind",
                                "I-prod.media",
                                "_",
                            ]
                        )
                    ),
                    "NEL_LIT_ID": datasets.Sequence(datasets.Value("string")),
                    "NEL_METO_ID": datasets.Sequence(datasets.Value("string")),
                    "no_space_after": datasets.Sequence(datasets.Value("bool")),
                    "end_of_line": datasets.Sequence(datasets.Value("bool")),
                    "EndOfSentence":datasets.Sequence(datasets.Value("bool")),
                    "date": datasets.Value("timestamp[s]"),
                    "title": datasets.Value("string"),
                    "document_id": datasets.Value("string"),
                }
            ),
            supervised_keys=None,
            homepage="TODO",
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        downloaded_files = dl_manager.download_and_extract(self.config.data_urls)
        data_files = {
            "dev": downloaded_files["dev"],
            "test": downloaded_files["test"],
        }
        splits = [
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={"filepath": data_files["dev"]},
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={"filepath": data_files["test"]},
            ),
        ]
        if self.config.name != "en":
            data_files.update({
                "train": downloaded_files["train"],
            })
            splits += [
                datasets.SplitGenerator(
                    name=datasets.Split.TRAIN,
                    gen_kwargs={"filepath": data_files["train"]},
                ),
            ]
        return splits

    def _generate_examples(self, filepath):
        date_re = re.compile(r"# date = (\d{4}-\d{2}-\d{02})")
        title_re = re.compile(r"newspaper = (\w{3})")
        document_id_re = re.compile(r"document_id = (.*)")
        with open(filepath, encoding="utf-8") as f:
            guid = 0
            tokens = []
            NE_COARSE_LIT_tags = []
            NE_COARSE_METO_tags = []
            NE_FINE_LIT_tags = []
            NE_FINE_METO_tags = []
            NE_FINE_COMP_tags = []
            NE_NESTED_tags = []
            NEL_LIT_ID = []
            NEL_METO_ID = []
            no_space_after = []
            end_of_line = []
            endofsentence = []

            new_sentence = False

            for line in f:
                if line.startswith(
                    "TOKEN	NE-COARSE-LIT	NE-COARSE-METO	NE-FINE-LIT	NE-FINE-METO	NE-FINE-COMP	NE-NESTED	NEL-LIT	NEL-METO	MISC"
                ):
                    continue
                if line.startswith("#") or line == "\n":
                    date_match = re.search(date_re, line)
                    if date_match:
                        date = date_match.group(1)
                        date = datetime.strptime(date, "%Y-%m-%d")
                    title_match = re.search(title_re, line)
                    if title_match:
                        title = title_match.group(1)
                    document_id_match = re.search(document_id_re, line)
                    if document_id_match:
                        document_id = document_id_match.group(1)
                    if tokens:
                        try:
                            date
                        except:
                            date = None
                        try:
                            title
                        except:
                            title = None
                        try:
                            document_id
                        except:
                            document_id = None
                        yield guid, {
                            "id": str(guid),
                            "tokens": tokens,
                            "NE_COARSE_LIT": NE_COARSE_LIT_tags,
                            "NE_COARSE_METO_tags": NE_COARSE_METO_tags,
                            "NE_FINE_LIT_tags": NE_FINE_LIT_tags,
                            "NE_FINE_METO_tags": NE_FINE_METO_tags,
                            "NE_FINE_COMP_tags": NE_FINE_COMP_tags,
                            "NE_NESTED_tags": NE_NESTED_tags,
                            "NEL_LIT_ID": NEL_LIT_ID,
                            "NEL_METO_ID": NEL_METO_ID,
                            "no_space_after": no_space_after,
                            "end_of_line": end_of_line,
                            "EndOfSentence":endofsentence,
                            "date": date,
                            "title": title,
                            "document_id": document_id,
                        }
                        guid += 1
                        tokens = []
                        NE_COARSE_LIT_tags = []
                        NE_COARSE_METO_tags = []
                        NE_FINE_LIT_tags = []
                        NE_FINE_METO_tags = []
                        NE_FINE_COMP_tags = []
                        NE_NESTED_tags = []
                        NEL_LIT_ID = []
                        NEL_METO_ID = []
                        no_space_after = []
                        end_of_line = []
                        endofsentence = []
                else:
                    # New row if there is a new sentence
                    if new_sentence == True:
                        if tokens:
                            try:
                                date
                            except:
                                date = None
                            try:
                                title
                            except:
                                title = None
                            try:
                                document_id
                            except:
                                document_id = None
                            yield guid, {
                                "id": str(guid),
                                "tokens": tokens,
                                "NE_COARSE_LIT": NE_COARSE_LIT_tags,
                                "NE_COARSE_METO_tags": NE_COARSE_METO_tags,
                                "NE_FINE_LIT_tags": NE_FINE_LIT_tags,
                                "NE_FINE_METO_tags": NE_FINE_METO_tags,
                                "NE_FINE_COMP_tags": NE_FINE_COMP_tags,
                                "NE_NESTED_tags": NE_NESTED_tags,
                                "NEL_LIT_ID": NEL_LIT_ID,
                                "NEL_METO_ID": NEL_METO_ID,
                                "no_space_after": no_space_after,
                                "end_of_line": end_of_line,
                                "EndOfSentence":endofsentence,
                                "date": date,
                                "title": title,
                                "document_id": document_id,
                            }
                            guid += 1
                            tokens = []
                            NE_COARSE_LIT_tags = []
                            NE_COARSE_METO_tags = []
                            NE_FINE_LIT_tags = []
                            NE_FINE_METO_tags = []
                            NE_FINE_COMP_tags = []
                            NE_NESTED_tags = []
                            NEL_LIT_ID = []
                            NEL_METO_ID = []
                            no_space_after = []
                            end_of_line = []
                            endofsentence = []

                    # HIPE 2020 tokens are tab separated
                    splits = line.split(
                        "\t"
                    )  # TOKEN	NE-COARSE-LIT	NE-COARSE-METO	NE-FINE-LIT	NE-FINE-METO	NE-FINE-COMP	NE-NESTED	NEL-LIT	NEL-METO	MISC
                    tokens.append(splits[0])
                    NE_COARSE_LIT_tags.append(splits[1])
                    NE_COARSE_METO_tags.append(splits[2])
                    NE_FINE_LIT_tags.append(splits[3])
                    NE_FINE_METO_tags.append(splits[4])
                    NE_FINE_COMP_tags.append(splits[5])
                    NE_NESTED_tags.append(splits[6])
                    NEL_LIT_ID.append(splits[7])
                    NEL_METO_ID.append(splits[8])
                    misc = splits[-1]
                    is_space = "NoSpaceAfter" in misc
                    is_end_of_line = "EndOfLine" in misc
                    EndOfSentence = "EndOfSentence" in misc
                    no_space_after.append(is_space)
                    end_of_line.append(is_end_of_line)
                    endofsentence.append(EndOfSentence)

                    new_sentence = EndOfSentence

            # last example
            yield guid, {
                "id": str(guid),
                "tokens": tokens,
                "NE_COARSE_LIT": NE_COARSE_LIT_tags,
                "NE_COARSE_METO_tags": NE_COARSE_METO_tags,
                "NE_FINE_LIT_tags": NE_FINE_LIT_tags,
                "NE_FINE_METO_tags": NE_FINE_METO_tags,
                "NE_FINE_COMP_tags": NE_FINE_COMP_tags,
                "NE_NESTED_tags": NE_NESTED_tags,
                "NEL_LIT_ID": NEL_LIT_ID,
                "NEL_METO_ID": NEL_METO_ID,
                "no_space_after": no_space_after,
                "end_of_line": end_of_line,
                "EndOfSentence":endofsentence,
                "date": date,
                "title": title,
                "document_id": document_id,
            }
