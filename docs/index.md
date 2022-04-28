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

!!! notice tips "Known Issues"
    - Lists do not currently work.
    - codeblocks
    - Probably other things as well..
