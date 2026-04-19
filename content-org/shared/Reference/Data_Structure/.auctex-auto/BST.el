;; -*- lexical-binding: t; -*-

(TeX-add-style-hook
 "BST"
 (lambda ()
   (LaTeX-add-bibitems
    "enwiki:bst_tree"
    "enwiki:avl_tree"
    "adelson1962algorithm"))
 '(or :bibtex :latex))

