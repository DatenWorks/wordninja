![image](https://user-images.githubusercontent.com/2049665/29219793-b4dcb942-7e7e-11e7-8785-761b0e784e04.png)

Word Ninja
==========

Slice your munged together words!  Seriously, Take anything, `'imateapot'` for example, would become `['im', 'a', 'teapot']`.  Useful for humanizing stuff (like database tables when people don't like underscores).

This project is repackaging the excellent work from here: http://stackoverflow.com/a/11642687/2449774

Usage
-----
```
$ python
>>> import wordninja
>>> wordninja.split('somewords')
['some', 'words']
>>> wordninja.split('imateapot')
['im', 'a', 'teapot']
>>> wordninja.split('thequickbrownfoxjumpsoverthelazydog')
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

Performance
-----------
It's even faster!

```
>>> def f():
...   wordninja.split('imateapot')
... 
>>> timeit.timeit(f, number=10000)
0.14521459000236155
```

It can handle long strings:
```
>>>> hamlet_act3_scene1="ThatunmatchedformandfeatureofblownyouthBlastedwithecstasy.Oh,woeisme,T'haveseenwhatIhaveseen,seewhatIsee!".lower()
>>>> wordninja.split(hamlet_act3_scene1)
['that', 'unmatched', 'form', 'and', 'feature', 'of', 'blown', 'youth', 'blasted', 'with', 'ecstasy', 'oh', 'woe', 'is', 'me', 't', 'have', 'seen', 'what', 'i', 'have', 'seen', 'see', 'what', 'i', 'see']
>>>>
>>>> def f():
....     wordninja.split(hamlet_act3_scene1)
....
>>>> timeit.timeit(f, number=1)
0.005466152999360929
```
And scales well.  (This string took ~5ms to compute.)

How to Install
--------------

```
pip install -e git+https://github.com/macunha1/wordninja#egg=wordninja
```

