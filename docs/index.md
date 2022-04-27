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
The adnomitions python markdown extension needs to be added to your mkdocs.yml file.

```
markdown_extensions:
    - admonition
```

## General Markdown

  

### Blue Tip Callout
This is accomplished using admonitions with the `notice` and `tips` classes. To implement, the following syntax can be used.
```
    !!! notice tips "Optional Title"
        Notice text
```
!!! notice tips "Optional Title"
    Notice tip text

### Red Danger Callout
This is accomplished using admonitions with the `notice` and `danger` classes. To implement, the following syntax can be used.
```
    !!! notice danger "Optional Title"
        Notice text
```
!!! notice danger "Optional Title"
    Notice danger text

## Tables
Tables can be used with normal markdown syntax
```
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


# Known Issues
- Lists
- Drop Down/Show/Hide functionality
  - This can be implemented using the newer python `details` and `summary` elements however, these are not supported in the AS Help which would cause an issue should someone want to export for them.