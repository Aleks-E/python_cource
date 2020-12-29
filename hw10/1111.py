C:\Users\V\AppData\Local\Programs\Python\Python39\python.exe D:/EPAM_python_cource/Homework/python_cource/hw10/task_1.py
Help on class BeautifulSoup in module bs4:

class BeautifulSoup(bs4.element.Tag)
 |  BeautifulSoup(markup='', features=None, builder=None, parse_only=None, from_encoding=None, exclude_encodings=None, element_classes=None, **kwargs)
 |
 |  A data structure representing a parsed HTML or XML document.
 |
 |  Most of the methods you'll call on a BeautifulSoup object are inherited from
 |  PageElement or Tag.
 |
 |  Internally, this class defines the basic interface called by the
 |  tree builders when converting an HTML/XML document into a data
 |  structure. The interface abstracts away the differences between
 |  parsers. To write a new tree builder, you'll need to understand
 |  these methods as a whole.
 |
 |  These methods will be called by the BeautifulSoup constructor:
 |    * reset()
 |    * feed(markup)
 |
 |  The tree builder may call these methods from its feed() implementation:
 |    * handle_starttag(name, attrs) # See note about return value
 |    * handle_endtag(name)
 |    * handle_data(data) # Appends to the current data node
 |    * endData(containerClass) # Ends the current data node
 |
 |  No matter how complicated the underlying parser is, you should be
 |  able to build a tree using 'start tag' events, 'end tag' events,
 |  'data' events, and "done with data" events.
 |
 |  If you encounter an empty-element tag (aka a self-closing tag,
 |  like HTML's <br> tag), call handle_starttag and then
 |  handle_endtag.
 |
 |  Method resolution order:
 |      BeautifulSoup
 |      bs4.element.Tag
 |      bs4.element.PageElement
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __copy__(self)
 |      Copy a BeautifulSoup object by converting the document to a string and parsing it again.
 |
 |  __getstate__(self)
 |
 |  __init__(self, markup='', features=None, builder=None, parse_only=None, from_encoding=None, exclude_encodings=None, element_classes=None, **kwargs)
 |      Constructor.
 |
 |      :param markup: A string or a file-like object representing
 |       markup to be parsed.
 |
 |      :param features: Desirable features of the parser to be
 |       used. This may be the name of a specific parser ("lxml",
 |       "lxml-xml", "html.parser", or "html5lib") or it may be the
 |       type of markup to be used ("html", "html5", "xml"). It's
 |       recommended that you name a specific parser, so that
 |       Beautiful Soup gives you the same results across platforms
 |       and virtual environments.
 |
 |      :param builder: A TreeBuilder subclass to instantiate (or
 |       instance to use) instead of looking one up based on
 |       `features`. You only need to use this if you've implemented a
 |       custom TreeBuilder.
 |
 |      :param parse_only: A SoupStrainer. Only parts of the document
 |       matching the SoupStrainer will be considered. This is useful
 |       when parsing part of a document that would otherwise be too
 |       large to fit into memory.
 |
 |      :param from_encoding: A string indicating the encoding of the
 |       document to be parsed. Pass this in if Beautiful Soup is
 |       guessing wrongly about the document's encoding.
 |
 |      :param exclude_encodings: A list of strings indicating
 |       encodings known to be wrong. Pass this in if you don't know
 |       the document's encoding but you know Beautiful Soup's guess is
 |       wrong.
 |
 |      :param element_classes: A dictionary mapping BeautifulSoup
 |       classes like Tag and NavigableString, to other classes you'd
 |       like to be instantiated instead as the parse tree is
 |       built. This is useful for subclassing Tag or NavigableString
 |       to modify default behavior.
 |
 |      :param kwargs: For backwards compatibility purposes, the
 |       constructor accepts certain keyword arguments used in
 |       Beautiful Soup 3. None of these arguments do anything in
 |       Beautiful Soup 4; they will result in a warning and then be
 |       ignored.
 |
 |       Apart from this, any keyword arguments passed into the
 |       BeautifulSoup constructor are propagated to the TreeBuilder
 |       constructor. This makes it possible to configure a
 |       TreeBuilder by passing in arguments, not just by saying which
 |       one to use.
 |
 |  decode(self, pretty_print=False, eventual_encoding='utf-8', formatter='minimal')
 |      Returns a string or Unicode representation of the parse tree
 |          as an HTML or XML document.
 |
 |      :param pretty_print: If this is True, indentation will be used to
 |          make the document more readable.
 |      :param eventual_encoding: The encoding of the final document.
 |          If this is None, the document will be a Unicode string.
 |
 |  endData(self, containerClass=None)
 |      Method called by the TreeBuilder when the end of a data segment
 |      occurs.
 |
 |  handle_data(self, data)
 |      Called by the tree builder when a chunk of textual data is encountered.
 |
 |  handle_endtag(self, name, nsprefix=None)
 |      Called by the tree builder when an ending tag is encountered.
 |
 |      :param name: Name of the tag.
 |      :param nsprefix: Namespace prefix for the tag.
 |
 |  handle_starttag(self, name, namespace, nsprefix, attrs, sourceline=None, sourcepos=None)
 |      Called by the tree builder when a new tag is encountered.
 |
 |      :param name: Name of the tag.
 |      :param nsprefix: Namespace prefix for the tag.
 |      :param attrs: A dictionary of attribute values.
 |      :param sourceline: The line number where this tag was found in its
 |          source document.
 |      :param sourcepos: The character position within `sourceline` where this
 |          tag was found.
 |
 |      If this method returns None, the tag was rejected by an active
 |      SoupStrainer. You should proceed as if the tag had not occurred
 |      in the document. For instance, if this was a self-closing tag,
 |      don't call handle_endtag.
 |
 |  insert_after(self, *args)
 |      This method is part of the PageElement API, but `BeautifulSoup` doesn't implement
 |      it because there is nothing before or after it in the parse tree.
 |
 |  insert_before(self, *args)
 |      This method is part of the PageElement API, but `BeautifulSoup` doesn't implement
 |      it because there is nothing before or after it in the parse tree.
 |
 |  new_string(self, s, subclass=None)
 |      Create a new NavigableString associated with this BeautifulSoup
 |      object.
 |
 |  new_tag(self, name, namespace=None, nsprefix=None, attrs={}, sourceline=None, sourcepos=None, **kwattrs)
 |      Create a new Tag associated with this BeautifulSoup object.
 |
 |      :param name: The name of the new Tag.
 |      :param namespace: The URI of the new Tag's XML namespace, if any.
 |      :param prefix: The prefix for the new Tag's XML namespace, if any.
 |      :param attrs: A dictionary of this Tag's attribute values; can
 |          be used instead of `kwattrs` for attributes like 'class'
 |          that are reserved words in Python.
 |      :param sourceline: The line number where this tag was
 |          (purportedly) found in its source document.
 |      :param sourcepos: The character position within `sourceline` where this
 |          tag was (purportedly) found.
 |      :param kwattrs: Keyword arguments for the new Tag's attribute values.
 |
 |  object_was_parsed(self, o, parent=None, most_recent_element=None)
 |      Method called by the TreeBuilder to integrate an object into the parse tree.
 |
 |  popTag(self)
 |      Internal method called by _popToTag when a tag is closed.
 |
 |  pushTag(self, tag)
 |      Internal method called by handle_starttag when a tag is opened.
 |
 |  reset(self)
 |      Reset this object to a state as though it had never parsed any
 |      markup.
 |
 |  string_container(self, base_class=None)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  ASCII_SPACES = ' \n\t\x0c\r'
 |
 |  DEFAULT_BUILDER_FEATURES = ['html', 'fast']
 |
 |  NO_PARSER_SPECIFIED_WARNING = 'No parser was explicitly specified, so ...
 |
 |  ROOT_TAG_NAME = '[document]'
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from bs4.element.Tag:
 |
 |  __bool__(self)
 |      A tag is non-None even if it has no contents.
 |
 |  __call__(self, *args, **kwargs)
 |      Calling a Tag like a function is the same as calling its
 |      find_all() method. Eg. tag('a') returns a list of all the A tags
 |      found within this tag.
 |
 |  __contains__(self, x)
 |
 |  __delitem__(self, key)
 |      Deleting tag[key] deletes all 'key' attributes for the tag.
 |
 |  __eq__(self, other)
 |      Returns true iff this Tag has the same name, the same attributes,
 |      and the same contents (recursively) as `other`.
 |
 |  __getattr__(self, tag)
 |      Calling tag.subtag is the same as calling tag.find(name="subtag")
 |
 |  __getitem__(self, key)
 |      tag[key] returns the value of the 'key' attribute for the Tag,
 |      and throws an exception if it's not there.
 |
 |  __hash__(self)
 |      Return hash(self).
 |
 |  __iter__(self)
 |      Iterating over a Tag iterates over its contents.
 |
 |  __len__(self)
 |      The length of a Tag is the length of its list of contents.
 |
 |  __ne__(self, other)
 |      Returns true iff this Tag is not identical to `other`,
 |      as defined in __eq__.
 |
 |  __repr__ = __unicode__(self)
 |
 |  __setitem__(self, key, value)
 |      Setting tag[key] sets the value of the 'key' attribute for the
 |      tag.
 |
 |  __str__ = __unicode__(self)
 |
 |  __unicode__(self)
 |      Renders this PageElement as a Unicode string.
 |
 |  childGenerator(self)
 |      Deprecated generator.
 |
 |  clear(self, decompose=False)
 |      Wipe out all children of this PageElement by calling extract()
 |         on them.
 |
 |      :param decompose: If this is True, decompose() (a more
 |          destructive method) will be called instead of extract().
 |
 |  decode_contents(self, indent_level=None, eventual_encoding='utf-8', formatter='minimal')
 |      Renders the contents of this tag as a Unicode string.
 |
 |      :param indent_level: Each line of the rendering will be
 |         indented this many spaces. Used internally in
 |         recursive calls while pretty-printing.
 |
 |      :param eventual_encoding: The tag is destined to be
 |         encoded into this encoding. decode_contents() is _not_
 |         responsible for performing that encoding. This information
 |         is passed in so that it can be substituted in if the
 |         document contains a <META> tag that mentions the document's
 |         encoding.
 |
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard Formatters.
 |
 |  decompose(self)
 |      Recursively destroys this PageElement and its children.
 |
 |      This element will be removed from the tree and wiped out; so
 |      will everything beneath it.
 |
 |      The behavior of a decomposed PageElement is undefined and you
 |      should never use one for anything, but if you need to _check_
 |      whether an element has been decomposed, you can use the
 |      `decomposed` property.
 |
 |  encode(self, encoding='utf-8', indent_level=None, formatter='minimal', errors='xmlcharrefreplace')
 |      Render a bytestring representation of this PageElement and its
 |      contents.
 |
 |      :param encoding: The destination encoding.
 |      :param indent_level: Each line of the rendering will be
 |          indented this many spaces. Used internally in
 |          recursive calls while pretty-printing.
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard formatters.
 |      :param errors: An error handling strategy such as
 |          'xmlcharrefreplace'. This value is passed along into
 |          encode() and its value should be one of the constants
 |          defined by Python.
 |      :return: A bytestring.
 |
 |  encode_contents(self, indent_level=None, encoding='utf-8', formatter='minimal')
 |      Renders the contents of this PageElement as a bytestring.
 |
 |      :param indent_level: Each line of the rendering will be
 |         indented this many spaces. Used internally in
 |         recursive calls while pretty-printing.
 |
 |      :param eventual_encoding: The bytestring will be in this encoding.
 |
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard Formatters.
 |
 |      :return: A bytestring.
 |
 |  find(self, name=None, attrs={}, recursive=True, text=None, **kwargs)
 |      Look in the children of this PageElement and find the first
 |      PageElement that matches the given criteria.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param recursive: If this is True, find() will perform a
 |          recursive search of this PageElement's children. Otherwise,
 |          only the direct children will be considered.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  findAll = find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
 |
 |  findChild = find(self, name=None, attrs={}, recursive=True, text=None, **kwargs)
 |
 |  findChildren = find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
 |
 |  find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs)
 |      Look in the children of this PageElement and find all
 |      PageElements that match the given criteria.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param recursive: If this is True, find_all() will perform a
 |          recursive search of this PageElement's children. Otherwise,
 |          only the direct children will be considered.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |
 |  get(self, key, default=None)
 |      Returns the value of the 'key' attribute for the tag, or
 |      the value given for 'default' if it doesn't have that
 |      attribute.
 |
 |  getText = get_text(self, separator='', strip=False, types=(<class 'bs4.element.NavigableString'>, <class 'bs4.element.CData'>))
 |
 |  get_attribute_list(self, key, default=None)
 |      The same as get(), but always returns a list.
 |
 |      :param key: The attribute to look for.
 |      :param default: Use this value if the attribute is not present
 |          on this PageElement.
 |      :return: A list of values, probably containing only a single
 |          value.
 |
 |  get_text(self, separator='', strip=False, types=(<class 'bs4.element.NavigableString'>, <class 'bs4.element.CData'>))
 |      Get all child strings, concatenated using the given separator.
 |
 |      :param separator: Strings will be concatenated using this separator.
 |
 |      :param strip: If True, strings will be stripped before being
 |          concatenated.
 |
 |      :types: A tuple of NavigableString subclasses. Any strings of
 |          a subclass not found in this list will be ignored. By
 |          default, this means only NavigableString and CData objects
 |          will be considered. So no comments, processing instructions,
 |          stylesheets, etc.
 |
 |      :return: A string.
 |
 |  has_attr(self, key)
 |      Does this PageElement have an attribute with the given name?
 |
 |  has_key(self, key)
 |      Deprecated method. This was kind of misleading because has_key()
 |      (attributes) was different from __in__ (contents).
 |
 |      has_key() is gone in Python 3, anyway.
 |
 |  index(self, element)
 |      Find the index of a child by identity, not value.
 |
 |      Avoids issues with tag.contents.index(element) getting the
 |      index of equal elements.
 |
 |      :param element: Look for this PageElement in `self.contents`.
 |
 |  prettify(self, encoding=None, formatter='minimal')
 |      Pretty-print this PageElement as a string.
 |
 |      :param encoding: The eventual encoding of the string. If this is None,
 |          a Unicode string will be returned.
 |      :param formatter: A Formatter object, or a string naming one of
 |          the standard formatters.
 |      :return: A Unicode string (if encoding==None) or a bytestring
 |          (otherwise).
 |
 |  recursiveChildGenerator(self)
 |      Deprecated generator.
 |
 |  renderContents(self, encoding='utf-8', prettyPrint=False, indentLevel=0)
 |      Deprecated method for BS3 compatibility.
 |
 |  select(self, selector, namespaces=None, limit=None, **kwargs)
 |      Perform a CSS selection operation on the current element.
 |
 |      This uses the SoupSieve library.
 |
 |      :param selector: A string containing a CSS selector.
 |
 |      :param namespaces: A dictionary mapping namespace prefixes
 |         used in the CSS selector to namespace URIs. By default,
 |         Beautiful Soup will use the prefixes it encountered while
 |         parsing the document.
 |
 |      :param limit: After finding this number of results, stop looking.
 |
 |      :param kwargs: Keyword arguments to be passed into SoupSieve's
 |         soupsieve.select() method.
 |
 |      :return: A ResultSet of Tags.
 |      :rtype: bs4.element.ResultSet
 |
 |  select_one(self, selector, namespaces=None, **kwargs)
 |      Perform a CSS selection operation on the current element.
 |
 |      :param selector: A CSS selector.
 |
 |      :param namespaces: A dictionary mapping namespace prefixes
 |         used in the CSS selector to namespace URIs. By default,
 |         Beautiful Soup will use the prefixes it encountered while
 |         parsing the document.
 |
 |      :param kwargs: Keyword arguments to be passed into SoupSieve's
 |         soupsieve.select() method.
 |
 |      :return: A Tag.
 |      :rtype: bs4.element.Tag
 |
 |  smooth(self)
 |      Smooth out this element's children by consolidating consecutive
 |      strings.
 |
 |      This makes pretty-printed output look more natural following a
 |      lot of operations that modified the tree.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from bs4.element.Tag:
 |
 |  children
 |      Iterate over all direct children of this PageElement.
 |
 |      :yield: A sequence of PageElements.
 |
 |  descendants
 |      Iterate over all children of this PageElement in a
 |      breadth-first sequence.
 |
 |      :yield: A sequence of PageElements.
 |
 |  isSelfClosing
 |      Is this tag an empty-element tag? (aka a self-closing tag)
 |
 |      A tag that has contents is never an empty-element tag.
 |
 |      A tag that has no contents may or may not be an empty-element
 |      tag. It depends on the builder used to create the tag. If the
 |      builder has a designated list of empty-element tags, then only
 |      a tag whose name shows up in that list is considered an
 |      empty-element tag.
 |
 |      If the builder has no designated list of empty-element tags,
 |      then any tag with no contents is an empty-element tag.
 |
 |  is_empty_element
 |      Is this tag an empty-element tag? (aka a self-closing tag)
 |
 |      A tag that has contents is never an empty-element tag.
 |
 |      A tag that has no contents may or may not be an empty-element
 |      tag. It depends on the builder used to create the tag. If the
 |      builder has a designated list of empty-element tags, then only
 |      a tag whose name shows up in that list is considered an
 |      empty-element tag.
 |
 |      If the builder has no designated list of empty-element tags,
 |      then any tag with no contents is an empty-element tag.
 |
 |  strings
 |      Yield all strings of certain classes, possibly stripping them.
 |
 |      :param strip: If True, all strings will be stripped before being
 |          yielded.
 |
 |      :types: A tuple of NavigableString subclasses. Any strings of
 |          a subclass not found in this list will be ignored. By
 |          default, this means only NavigableString and CData objects
 |          will be considered. So no comments, processing instructions,
 |          etc.
 |
 |      :yield: A sequence of strings.
 |
 |  stripped_strings
 |      Yield all strings in the document, stripping them first.
 |
 |      :yield: A sequence of stripped strings.
 |
 |  text
 |      Get all child strings, concatenated using the given separator.
 |
 |      :param separator: Strings will be concatenated using this separator.
 |
 |      :param strip: If True, strings will be stripped before being
 |          concatenated.
 |
 |      :types: A tuple of NavigableString subclasses. Any strings of
 |          a subclass not found in this list will be ignored. By
 |          default, this means only NavigableString and CData objects
 |          will be considered. So no comments, processing instructions,
 |          stylesheets, etc.
 |
 |      :return: A string.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from bs4.element.Tag:
 |
 |  parserClass
 |
 |  string
 |      Convenience property to get the single string within this
 |      PageElement.
 |
 |      TODO It might make sense to have NavigableString.string return
 |      itself.
 |
 |      :return: If this element has a single string child, return
 |       value is that string. If this element has one child tag,
 |       return value is the 'string' attribute of the child tag,
 |       recursively. If this element is itself a string, has no
 |       children, or has more than one child, return value is None.
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from bs4.element.PageElement:
 |
 |  append(self, tag)
 |      Appends the given PageElement to the contents of this one.
 |
 |      :param tag: A PageElement.
 |
 |  extend(self, tags)
 |      Appends the given PageElements to this one's contents.
 |
 |      :param tags: A list of PageElements.
 |
 |  extract(self, _self_index=None)
 |      Destructively rips this element out of the tree.
 |
 |      :param _self_index: The location of this element in its parent's
 |         .contents, if known. Passing this in allows for a performance
 |         optimization.
 |
 |      :return: `self`, no longer part of the tree.
 |
 |  fetchNextSiblings = find_next_siblings(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |
 |  fetchParents = find_parents(self, name=None, attrs={}, limit=None, **kwargs)
 |
 |  fetchPrevious = find_all_previous(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |
 |  fetchPreviousSiblings = find_previous_siblings(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |
 |  findAllNext = find_all_next(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |
 |  findAllPrevious = find_all_previous(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |
 |  findNext = find_next(self, name=None, attrs={}, text=None, **kwargs)
 |
 |  findNextSibling = find_next_sibling(self, name=None, attrs={}, text=None, **kwargs)
 |
 |  findNextSiblings = find_next_siblings(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |
 |  findParent = find_parent(self, name=None, attrs={}, **kwargs)
 |
 |  findParents = find_parents(self, name=None, attrs={}, limit=None, **kwargs)
 |
 |  findPrevious = find_previous(self, name=None, attrs={}, text=None, **kwargs)
 |
 |  findPreviousSibling = find_previous_sibling(self, name=None, attrs={}, text=None, **kwargs)
 |
 |  findPreviousSiblings = find_previous_siblings(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |
 |  find_all_next(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |      Find all PageElements that match the given criteria and appear
 |      later in the document than this PageElement.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet containing PageElements.
 |
 |  find_all_previous(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |      Look backwards in the document from this PageElement and find all
 |      PageElements that match the given criteria.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |
 |  find_next(self, name=None, attrs={}, text=None, **kwargs)
 |      Find the first PageElement that matches the given criteria and
 |      appears later in the document than this PageElement.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  find_next_sibling(self, name=None, attrs={}, text=None, **kwargs)
 |      Find the closest sibling to this PageElement that matches the
 |      given criteria and appears later in the document.
 |
 |      All find_* methods take a common set of arguments. See the
 |      online documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  find_next_siblings(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |      Find all siblings of this PageElement that match the given criteria
 |      and appear later in the document.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |
 |  find_parent(self, name=None, attrs={}, **kwargs)
 |      Find the closest parent of this PageElement that matches the given
 |      criteria.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :kwargs: A dictionary of filters on attribute values.
 |
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  find_parents(self, name=None, attrs={}, limit=None, **kwargs)
 |      Find all parents of this PageElement that match the given criteria.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  find_previous(self, name=None, attrs={}, text=None, **kwargs)
 |      Look backwards in the document from this PageElement and find the
 |      first PageElement that matches the given criteria.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  find_previous_sibling(self, name=None, attrs={}, text=None, **kwargs)
 |      Returns the closest sibling to this PageElement that matches the
 |      given criteria and appears earlier in the document.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  find_previous_siblings(self, name=None, attrs={}, text=None, limit=None, **kwargs)
 |      Returns all siblings to this PageElement that match the
 |      given criteria and appear earlier in the document.
 |
 |      All find_* methods take a common set of arguments. See the online
 |      documentation for detailed explanations.
 |
 |      :param name: A filter on tag name.
 |      :param attrs: A dictionary of filters on attribute values.
 |      :param text: A filter for a NavigableString with specific text.
 |      :param limit: Stop looking after finding this many results.
 |      :kwargs: A dictionary of filters on attribute values.
 |      :return: A ResultSet of PageElements.
 |      :rtype: bs4.element.ResultSet
 |
 |  format_string(self, s, formatter)
 |      Format the given string using the given formatter.
 |
 |      :param s: A string.
 |      :param formatter: A Formatter object, or a string naming one of the standard formatters.
 |
 |  formatter_for_name(self, formatter)
 |      Look up or create a Formatter for the given identifier,
 |      if necessary.
 |
 |      :param formatter: Can be a Formatter object (used as-is), a
 |          function (used as the entity substitution hook for an
 |          XMLFormatter or HTMLFormatter), or a string (used to look
 |          up an XMLFormatter or HTMLFormatter in the appropriate
 |          registry.
 |
 |  insert(self, position, new_child)
 |      Insert a new PageElement in the list of this PageElement's children.
 |
 |      This works the same way as `list.insert`.
 |
 |      :param position: The numeric position that should be occupied
 |         in `self.children` by the new PageElement.
 |      :param new_child: A PageElement.
 |
 |  nextGenerator(self)
 |      # Old non-property versions of the generators, for backwards
 |      # compatibility with BS3.
 |
 |  nextSiblingGenerator(self)
 |
 |  parentGenerator(self)
 |
 |  previousGenerator(self)
 |
 |  previousSiblingGenerator(self)
 |
 |  replaceWith = replace_with(self, replace_with)
 |
 |  replaceWithChildren = unwrap(self)
 |
 |  replace_with(self, replace_with)
 |      Replace this PageElement with another one, keeping the rest of the
 |      tree the same.
 |
 |      :param replace_with: A PageElement.
 |      :return: `self`, no longer part of the tree.
 |
 |  replace_with_children = unwrap(self)
 |
 |  setup(self, parent=None, previous_element=None, next_element=None, previous_sibling=None, next_sibling=None)
 |      Sets up the initial relations between this element and
 |      other elements.
 |
 |      :param parent: The parent of this element.
 |
 |      :param previous_element: The element parsed immediately before
 |          this one.
 |
 |      :param next_element: The element parsed immediately before
 |          this one.
 |
 |      :param previous_sibling: The most recently encountered element
 |          on the same level of the parse tree as this one.
 |
 |      :param previous_sibling: The next element to be encountered
 |          on the same level of the parse tree as this one.
 |
 |  unwrap(self)
 |      Replace this PageElement with its contents.
 |
 |      :return: `self`, no longer part of the tree.
 |
 |  wrap(self, wrap_inside)
 |      Wrap this PageElement inside another one.
 |
 |      :param wrap_inside: A PageElement.
 |      :return: `wrap_inside`, occupying the position in the tree that used
 |         to be occupied by `self`, and with `self` inside it.
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from bs4.element.PageElement:
 |
 |  decomposed
 |      Check whether a PageElement has been decomposed.
 |
 |      :rtype: bool
 |
 |  next
 |      The PageElement, if any, that was parsed just after this one.
 |
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  next_elements
 |      All PageElements that were parsed after this one.
 |
 |      :yield: A sequence of PageElements.
 |
 |  next_siblings
 |      All PageElements that are siblings of this one but were parsed
 |      later.
 |
 |      :yield: A sequence of PageElements.
 |
 |  parents
 |      All PageElements that are parents of this PageElement.
 |
 |      :yield: A sequence of PageElements.
 |
 |  previous
 |      The PageElement, if any, that was parsed just before this one.
 |
 |      :return: A PageElement.
 |      :rtype: bs4.element.Tag | bs4.element.NavigableString
 |
 |  previous_elements
 |      All PageElements that were parsed before this one.
 |
 |      :yield: A sequence of PageElements.
 |
 |  previous_siblings
 |      All PageElements that are siblings of this one but were parsed
 |      earlier.
 |
 |      :yield: A sequence of PageElements.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from bs4.element.PageElement:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  nextSibling
 |
 |  previousSibling

None

Process finished with exit code 0
