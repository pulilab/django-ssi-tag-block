django-ssi-tag-block
====================

This is a simple test django project to show unexpected behavior wrt. django's {% ssi %} and {% block %} tags.

Check out the templates to get an understanding of what the test is about. I would expect the text "Everything fine. The content block was overwritten!" to be rendered, but "This is the original content block. You should never see me." shows up on the screen.

Tested under django 1.5.5
