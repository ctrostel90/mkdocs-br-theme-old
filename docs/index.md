# B&R Industrial Automation Theme

This is a base theme for use with MkDocs in the style of B&R Industrial Automation's documentation. You can see the style in action with this documentation. 

!!! notice danger "CSS and HTML Incompatibilities"
    It should be noted, that much of the style requirements are such to be able to support exporting for the AS Help as well as for standard webbrowsers. Because of this, many CSS or HTML elements may not be supported

## Installation
```
pip install mkdocs-br-industrial-theme
```

## Using The Theme
In your mkdown.yml file set the theme usnig name brtheme.
```
theme:
    name: brtheme
```
## Extensions
The adnomitions and pymdownx.details python markdown extension needs to be added to your mkdocs.yml file.

``` yaml
markdown_extensions:
    - admonition
    - pymdownx.details
```

## General Markdown

### Lists
It is possible to create basic lists with normal markdown syntax:

```
    - List Item 1
    - Item 2
    - Here ya go
```

- List Item 1
- Item 2
- Here ya go

As with most markdown, make sure to include extra whitespace above the list to have the styling work.

### Blue Tip Callout
This is accomplished using admonitions with the `notice` and `tips` classes. To implement, the following syntax can be used.
``` markdown
    !!! notice tips "Optional Title"
        Notice text
```
!!! notice tips "Optional Title"
    Notice tip text

### Red Danger Callout
This is accomplished using admonitions with the `notice` and `danger` classes. To implement, the following syntax can be used.
``` markdown
    !!! notice danger "Optional Title"
        Notice text
```
!!! notice danger "Optional Title"
    Notice danger text

## Tables
Tables can be used with normal markdown syntax
``` markdown
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

## DropDown
Drop down dynamic show/hide elements are also supported. This is accomplished using the markdown extension `details`.  To create a drop down the following syntax must be used:
``` markdown
    ??? dropdown-ct "Optional Title"
        Make sure to use include the dropdown-ct class name.
```
??? dropdown-ct "Optional Title"
    Make sure to use include the dropdown-ct class name.

    You should be able to embed numerous of these levels as well.
    
    ??? dropdown-ct "Another One"
        One more time.


[Known Issues](Known%20Issues.md)