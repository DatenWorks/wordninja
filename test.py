import unittest
import wordninja


class TestWordNinja(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(list(wordninja.split('derekanderson')),
                         ['derek', 'anderson'])

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
        self.assertEqual(list(wordninja.split('derek anderson')),
                         ['derek', 'anderson'])
        self.assertEqual(list(wordninja.split('derek-anderson')),
                         ['derek', 'anderson'])
        self.assertEqual(list(wordninja.split('derek_anderson')),
                         ['derek', 'anderson'])
        self.assertEqual(list(wordninja.split('derek/anderson')),
                         ['derek', 'anderson'])


if __name__ == '__main__':
    unittest.main()
