$(function() {
    'use strict';
    var counter = 1;
    var fields = {
        'id': 'thesenId',
        'title': 'thesenTitel',
        'argument': 'thesenArgument',
        'fazit': 'thesenFazit',
        'time': 'thesenTime'
    };
    InfiniteScroll.getData('discussions/?page=' + counter, content_card_home, fields);
    window.onscroll = function(e) {
        var scrollPosition = window.innerHeight + window.scrollY;
        var documentHeight = document.documentElement.scrollHeight;
        if (scrollPosition >= documentHeight) {
            counter++;
            console.log((counter-1)*5);
            if((counter-1)*5 < thesenCount)
                InfiniteScroll.getData('discussions/?page=' + counter, content_card_home, fields);
        }
    };
});