# Heading 1 The Largest Heading

Spacing needs to be specific. Line breaks are important.
If the markdown doesnt have a line *in-between
*italics* or _italicsAlt_.

**Bold** or __BoldAlt__.

**combination bold and _italics_**.

~~strikethrough.~~

## Lists

1. item
2. Incorrect numbers are corrected
    * Unordered sub-list
    * Unordered list item
        * sub item
3. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

## Links

[inline-style link](https://www.google.com)

[inline-style link with title](https://www.google.com "Google's Homepage")

[reference-style link][Arbitrary case-insensitive reference text]

[relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links.
http://www.example.com or <http://www.example.com> and sometimes
example.com (but not on Github, for example).

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

## Images

Inline-style:
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style:
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

## Code Syntax Highlights

Inline `code` has `back-ticks around` it.

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

```python
s = "Python syntax highlighting"
print s
```

```
Code Blocks should have a language tag
```

~~~~ text
code block
~~~~

## Tables

Tables aren't part of the core Markdown spec, but they are part of GFM(Gihub Flavored Markdown)

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

## Blockquotes

> Quoted text.
> > Quoted quote.

> * Quoted
> * List

## Horizontal Rules

---
***
___
