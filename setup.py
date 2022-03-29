#!/usr/bin/env python

import os

from setuptools import find_packages, setup

VERSION = os.getenv("CI_COMMIT_TAG")
if not VERSION:
    VERSION = "0.0.1"

# --- >
setup(
    name="skill-museum-guide",
    version=VERSION,
    package_dir={'skill_museum_guide': 'src/skill_museum_guide'},
    python_requires=">=3.6.8",
    packages=find_packages(where='src', include=['skill_museum_guide']),
    url="https://gitlab.com/mailru-voice/external_skills/skill_museum_guide",
    license="MIT",
    author="n.orgeev",
    author_email="n.orgeev@corp.mail.ru",
    description="skill-museum-guide",
)

