# encoding: utf-8

"""
Test suite for pptx.oxml.shapetree module
"""

from __future__ import absolute_import, print_function

import pytest

from pptx.oxml.autoshape import CT_Shape
from pptx.oxml.picture import CT_Picture
from pptx.oxml.shapetree import CT_GroupShape

from .unitdata.shape import an_spTree
from ..unitutil import class_mock, instance_mock, method_mock


class DescribeCT_GroupShape(object):

    def it_can_add_a_pic_element_representing_a_picture(self, add_pic_fixt):
        spTree, id_, name, desc, rId, x, y, cx, cy = add_pic_fixt[:9]
        CT_Picture_, insert_element_before_, pic_ = add_pic_fixt[9:]
        pic = spTree.add_pic(id_, name, desc, rId, x, y, cx, cy)
        CT_Picture_.new_pic.assert_called_once_with(
            id_, name, desc, rId, x, y, cx, cy
        )
        insert_element_before_.assert_called_once_with(pic_, 'p:extLst')
        assert pic is pic_

    def it_can_add_an_sp_element_for_an_autoshape(self, add_autoshape_fixt):
        spTree, id_, name, prst, x, y, cx, cy = add_autoshape_fixt[:8]
        CT_Shape_, insert_element_before_, sp_ = add_autoshape_fixt[8:]
        sp = spTree.add_autoshape(id_, name, prst, x, y, cx, cy)
        CT_Shape_.new_autoshape_sp.assert_called_once_with(
            id_, name, prst, x, y, cx, cy
        )
        insert_element_before_.assert_called_once_with(sp_, 'p:extLst')
        assert sp is sp_

    # fixtures ---------------------------------------------

    @pytest.fixture
    def add_pic_fixt(
            self, spTree, CT_Picture_, insert_element_before_, pic_):
        id_, name, desc, rId = 42, 'name', 'desc', 'rId6'
        x, y, cx, cy = 6, 7, 8, 9
        return (
            spTree, id_, name, desc, rId, x, y, cx, cy, CT_Picture_,
            insert_element_before_, pic_
        )

    @pytest.fixture
    def add_autoshape_fixt(
            self, spTree, CT_Shape_, insert_element_before_, sp_):
        id_, name, prst = 42, 'name', 'prst'
        x, y, cx, cy = 9, 8, 7, 6
        return (
            spTree, id_, name, prst, x, y, cx, cy, CT_Shape_,
            insert_element_before_, sp_
        )

    # fixture components -----------------------------------

    @pytest.fixture
    def CT_Picture_(self, request, pic_):
        CT_Picture_ = class_mock(request, 'pptx.oxml.shapetree.CT_Picture')
        CT_Picture_.new_pic.return_value = pic_
        return CT_Picture_

    @pytest.fixture
    def CT_Shape_(self, request, sp_):
        CT_Shape_ = class_mock(request, 'pptx.oxml.shapetree.CT_Shape')
        CT_Shape_.new_autoshape_sp.return_value = sp_
        return CT_Shape_

    @pytest.fixture
    def insert_element_before_(self, request):
        return method_mock(request, CT_GroupShape, 'insert_element_before')

    @pytest.fixture
    def pic_(self, request):
        return instance_mock(request, CT_Picture)

    @pytest.fixture
    def sp_(self, request):
        return instance_mock(request, CT_Shape)

    @pytest.fixture
    def spTree(self):
        return an_spTree().with_nsdecls().element
