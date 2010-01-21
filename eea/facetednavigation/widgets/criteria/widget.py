""" Criteria widget
"""
from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from eea.facetednavigation.widgets.widget import Widget as AbstractWidget

class Widget(AbstractWidget):
    """ Widget
    """
    # Widget properties
    widget_type = 'criteria'
    widget_label = 'Filters'
    view_js = '++resource++eea.facetednavigation.widgets.criteria.view.js'
    edit_js = '++resource++eea.facetednavigation.widgets.criteria.edit.js'
    view_css = '++resource++eea.facetednavigation.widgets.criteria.view.css'
    edit_css = '++resource++eea.facetednavigation.widgets.criteria.edit.css'

    index = ViewPageTemplateFile('widget.pt')
    edit_schema = AbstractWidget.edit_schema