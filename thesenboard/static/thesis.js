$(function() {
    'use strict';
    var counter = 1;
    var fields = {
        'id': 'thesisEntriesId',
        'title': 'thesisEntriesTitel',
        'argument': 'thesisEntriesArgument',
        'fazit': 'thesisEntriesFazit',
        'quelle': 'thesisEntriesQuelle',
        'time': 'thesisEntriesTime'
    };
    InfiniteScroll.getData('/discussion/'+id+'/?page=' + counter, content_card_discussion, fields);
    window.onscroll = function(e) {
        var scrollPosition = window.innerHeight + window.scrollY;
        var documentHeight = document.documentElement.scrollHeight;
        if (scrollPosition >= documentHeight) {
            counter++;
            if((counter-1)*5 < thesenCount)
                InfiniteScroll.getData('/discussion/'+id+'/?page=' + counter, content_card_discussion, fields);
        }
    };
});