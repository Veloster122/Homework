import pytest
import Converter



def test_make_nexus_data_header():
    known_inputs={'seq1':'ATGCAACACAGACCAGCACAAC','seq2': 'ATATATATATATATAATATATA'}
    expected_outputs='NEXUS\nBEGIN DATA;\nDIMENSIONS NTAX=2 NCHAR=22;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\n'
    for i, j in zip(known_inputs, expected_outputs):
        assert Converter.make_nexus_data_header(i) == j
        
def test_make_nexus_matrix():
    known_inputs={'seq1':'ATGCAACACAGACCAGCACAAC','seq2': 'ATATATATATATATAATATATA'}
    expected_outputs='seq1 ATGCAACACAGACCAGCACAAC\nseq2 ATATATATATATATAATATATA\n'
    for i, j in zip(known_inputs, expected_outputs):
        assert Converter.make_nexus_matrix(i) == j
        
def test_make_nexus_file():
    known_inputs={'seq1':'ATGCAACACAGACCAGCACAAC','seq2': 'ATATATATATATATAATATATA'}
    expected_outputs='NEXUS\nBEGIN DATA;\nDIMENSIONS NTAX=2 NCHAR=22;\nFORMAT DATATYPE=DNA MISSING=N GAP=-;\nMATRIX\nseq1 ATGCAACACAGACCAGCACAAC\nseq2 ATATATATATATATAATATATA\nEXIT;\n'
    for i, j in zip(known_inputs, expected_outputs):
        assert Converter.make_nexus_file(i) == j
        
        