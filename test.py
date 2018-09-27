# coding=utf-8
import re
import unittest
import wordninja


class TestWordNinja(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(list(wordninja.split('somewords')),
                         ['some', 'words'])


    def test_with_more_words(self):
        self.assertEqual(list(wordninja.split('somebiggergroupofwords')),
                         ['some', 'bigger', 'group', 'of', 'words'])


    def test_with_hamlet(self):
        act3_scene1 = """
        Thatunmatchedformandfeatureofblownyouth
        Blastedwithecstasy.Oh,woeisme,
        T'haveseenwhatIhaveseen,seewhatIsee!
        """.lower()
        __expected = ['that', 'unmatched', 'form', 'and', 'feature', 'of',
                      'blown', 'youth', 'blasted', 'with', 'ecstasy',
                      'oh', 'woe', 'is', 'me', 't', 'have', 'seen',
                      'what', 'i', 'have', 'seen', 'see', 'what', 'i', 'see']
        self.assertListEqual(wordninja.split(act3_scene1), __expected)


    def test_with_underscores_etc(self):
        self.assertEqual(list(wordninja.split('separated with space')),
                         ['separated', 'with', 'space'])
        self.assertEqual(list(wordninja.split('separated-with-dash')),
                         ['separated', 'with', 'dash'])
        self.assertEqual(list(wordninja.split('separated_with_underscore')),
                         ['separated', 'with', 'underscore'])
        self.assertEqual(list(wordninja.split('separated/with/slash')),
                         ['separated', 'with', 'slash'])


    def test_with_a_custom_regex(self):
        param = 'toseparate.ornottoseparate.com'
        custom_regex = re.compile("[^a-zA-Z0-9\.]+")
        self.assertNotEqual(wordninja.split(param, re=custom_regex),
                            wordninja.split(param))


if __name__ == '__main__':
    unittest.main()
