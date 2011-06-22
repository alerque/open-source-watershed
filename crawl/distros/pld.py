# -*- coding: utf-8 -*-
import subprocess
import time
import datetime
import os
from .utils import helper
from .utils.db import downstream
from .utils.types import Repo, DownstreamRelease

MIRROR = "ftp.pld-linux.org"
HTTP_START_DIR = None
FTP_START_DIR = None

ARCHES = ["i686","x86_64"]

distro_id = downstream.distro("pld", "", "A rolling release binay distribution.", "http://pld-linux.org")

# return a list of ["ubuntu", branch, codename, component, arch, None, None]
def get_repos(test):
	repos = []
	for comp in ["ac", "th", "ti"]:
		for a in ARCHES:
			repo = Repo()
			repo.distro_id = distro_id
			repo.component = comp
			repo.architecture = a
			repo.codename = ""
			repos.append(repo)
			downstream.repo(repo, test)
			downstream.add_branch(repo, "current", test)
	
			for comp-tree in ["ready", "test"]:
				repo = Repo()
				repo.distro_id = distro_id
				repo.component = comp + "-" + comptree
				repo.architecture = a
				repo.codename = ""
				repos.append(repo)
				downstream.repo(repo, test)
				downstream.add_branch(repo, "future", test)
	return repos

# return a list of [name, version, revision, epoch, time, extra]
def crawl_repo(repo):
	rels = []
  distro,branch,codename,component,arch,last_crawl,new = repo
  pass
