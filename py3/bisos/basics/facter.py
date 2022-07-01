# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: A /library/ to provide a cached and dictionary-like interface to Puppet's facter utility.
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]
*** Origins and related work.  https://github.com/knorby/facterpy
**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
*** A pure python library for reading in facter facts, caching them and making them available as python namedtuples.
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      This is a lower layer library which is then augmented by a CS-Lib and a CS.
**      [End-Of-Usage]
"""

icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current     :: Has been minimally tested. [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "pattern"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202110191256"
####+END:

####+BEGIN: bx:icm:py:status :status "Production"
icmInfo['status']  = "Production"
####+END:

icmInfo['credits'] = ""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/icmInfo-mbNedaGplByStar.py"
icmInfo['authors'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['copyright'] = "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]"
icmInfo['licenses'] = "[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"
icmInfo['maintainers'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['contacts'] = "[[http://mohsen.1.banan.byname.net/contact]]"
icmInfo['partOf'] = "[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]"
####+END:

icmInfo['panel'] = "{}-Panel.org".format(icmInfo['moduleName'])
icmInfo['groupingType'] = "IcmGroupingType-pkged"
icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"


####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/bisos/git/auth/bxRepos/bisos-pip/basics/py3/bisos/basics/pattern.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:

import json
import subprocess

import collections

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/importUcfIcmG.py"
from unisos import ucf
from unisos import icm

icm.unusedSuppressForEval(ucf.__file__)  # in case icm and ucf are not used

G = icm.IcmGlobalContext()
# G.icmLibsAppend = __file__
# G.icmCmndsLibsAppend = __file__
####+END:

_facterCacheEnabled = True

_facterCurCache = None

####+BEGIN: bx:icm:py3:func :funcName "_runFacterAndGetJsonOutputBytes" :funcType "" :retType "" :deco "" :argsList "" :comment ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /_runFacterAndGetJsonOutputBytes/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def _runFacterAndGetJsonOutputBytes(
####+END:
):
    """
** Run "facter --json". Get results as json bytes.
    """
    jsonOutputBytes = subprocess.check_output(['facter', '--json'])
    return jsonOutputBytes


####+BEGIN: bx:icm:py3:func :funcName "_dictToNamedTuple" :funcType "" :retType "" :deco "" :argsList "" :comment ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /_dictToNamedTuple/  [[elisp:(org-cycle)][| ]]
"""
def _dictToNamedTuple(
####+END:
        inDict,
):
    """
** Convert _inDict_ to  named tupples. Used as _json.loads(object_hook=dictToNamedTuple)_
    Called for each dictionary.
    """
    return collections.namedtuple('Facts', inDict.keys(), rename=True)(*inDict.values())


####+BEGIN: bx:icm:py3:func :funcName "_runFacterAndGetAllNamedTuple" :funcType "" :retType "" :deco "" :argsList "" :comment ""
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /_runFacterAndGetAllNamedTuple/  [[elisp:(org-cycle)][| ]]
"""
def _runFacterAndGetAllNamedTuple(
####+END:
):
    """
** Get facter as json and convert it to named tuples
    """
    jsonOutputBytes = _runFacterAndGetJsonOutputBytes()
    result = None
    try:
        result = json.loads(
            jsonOutputBytes,
            object_hook=_dictToNamedTuple,
        )
    except json.JSONDecodeError:
        icm.EH_critical_exception("json.JSONDecodeError")

    return result


####+BEGIN: bx:icm:py3:func :funcName "getAllAsNamedTuple" :funcType "" :retType "" :deco "" :argsList "" :comment "Instantiate specified class just once based on args."
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /getAllAsNamedTuple/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def getAllAsNamedTuple(
####+END:
        cache=True,
):
    """
** Get facter as json and convert it to named tuples
    """
    global _facterCurCache
    global _facterCacheEnabled

    if not _facterCacheEnabled:
        _facterCurCache = _runFacterAndGetAllNamedTuple()
    elif not _facterCurCache:
        _facterCurCache = _runFacterAndGetAllNamedTuple()
    elif not cache:
        _facterCurCache = _runFacterAndGetAllNamedTuple()
    else:
        pass

    return _facterCurCache

####+BEGIN: bx:icm:py3:func :funcName "get" :funcType "" :retType "" :deco "" :argsList "" :comment "Instantiate specified class just once based on args."
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /get/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def get(
####+END:
        factName,
        cache=True,
):
    """
** Get facter as json and convert it to named tuples.
*** Should not use eval here. Use getattr instead.
    """
    facts = getAllAsNamedTuple(cache=cache)

    try:
        factValue = eval(f"facts.{factName}")
    except AttributeError as e:
        icm.EH_critical_usageError(f"AttributeError -- Invalid factName={factName}")
        factValue = None
    except IndexError as e:
        icm.EH_critical_usageError(f"IndexError -- Invalid factName={factName}")
        factValue = None

    return factValue

####+BEGIN: bx:icm:py3:func :funcName "_getWithGetattrUnused" :funcType "" :retType "" :deco "" :argsList "" :comment "Instantiate specified class just once based on args."
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /_getWithGetattrUnused/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def _getWithGetattrUnused(
####+END:
        factName,
        cache=True,
):
    """
** Get facter as json and convert it to named tuples
    """
    facts = getAllAsNamedTuple(cache=cache)

    factNameList = factName.split(".")

    print(factNameList)

    curFacts = facts

    for each in factNameList:
        curFacts = getattr(curFacts, each)
        print(curFacts)

    return

####+BEGIN: bx:icm:py3:func :funcName "getOrDefault" :funcType "" :retType "" :deco "" :argsList "" :comment "Instantiate specified class just once based on args."
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /getOrDefault/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def getOrDefault(
####+END:
        factName,
        default,
        cache=True,
):
    """
** Get facter as json and convert it to named tuples.
    *** TODO dont use eval. Use getattr instead.
    """
    facts = getAllAsNamedTuple(cache=cache)

    try:
        factValue = eval(f"facts.{factName}")
    except AttributeError:
        factValue = default

    return factValue

####+BEGIN: bx:icm:py3:func :funcName "cacheAvailabilityToggle" :funcType "" :retType "" :deco "" :argsList "" :comment "Instantiate specified class just once based on args."
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /cacheAvailabilityToggle/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def cacheAvailabilityToggle(
####+END:
        enable=True,
):
    """
** Get facter as json and convert it to named tuples
    """
    global _facterCacheEnabled
    if enable:
        _facterCacheEnabled = True
    else:
        _facterCacheEnabled = False

####+BEGIN: bx:icm:py3:func :funcName "cacheAvailabilityObtain" :funcType "" :retType "" :deco "" :argsList "" :comment "Instantiate specified class just once based on args."
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /cacheAvailabilityObtain/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def cacheAvailabilityObtain(
####+END:
        enable=True,
):
    """
** Get facter as json and convert it to named tuples
    """
    global _facterCacheEnabled
    return _facterCacheEnabled


####+BEGIN: bx:icm:py3:func :funcName "_getNamedTupleOneLiner_unused" :funcType "" :retType "" :deco "" :argsList "" :comment "Instantiate specified class just once based on args."
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Func-      :: /_getNamedTupleOneLiner_unused/ =Instantiate specified class just once based on args.=  [[elisp:(org-cycle)][| ]]
"""
def _getNamedTupleOneLiner_unused(
####+END:
):
    """
** Get facter as json and convert it to named tuples
    """
    y = json.loads(subprocess.check_output(['facter', '--json']), object_hook=lambda d: collections.namedtuple('Factset', d.keys(), rename=True)(*d.values()))
    return y

####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
