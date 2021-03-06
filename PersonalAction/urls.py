from django.conf.urls import patterns, include, url

urlpatterns = patterns('PersonalAction.views',
    url(r'^status/$', 'status.Status', name='status'),
    url(r'borrow/$','borrowbook.Borrow',name="borrow"),
    url(r'borrow/(.+)/$','borrowbook.BorrowBook',name="borrowbook"),
    url(r'^status/(.+)/$','status.ReturnBook',name="return"),
    url(r'personalrecord/$','personalrecord.PersonalRecord',name="perRecord")
)
