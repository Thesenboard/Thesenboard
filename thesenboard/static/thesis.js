$(function() {
    'use strict';

    if(userId !== 'none') {
        poll.getData('/abstimmung/' + id + '/');

        var negativ = countAll - countPositives;

        var chartData = {
            labels: ["Pro", "Contra"],
            datasets: [{
                label: "Abstimmung",
                backgroundColor: [
                    '#28a745',
                    '#dc3545'
                ],
                data: [countPositives, negativ]
            }]
        };
        poll.drawChart(chartData);

        $(document).on('click', '.abstimmung', function () {
            var data = JSON.stringify({
                'thesisAbstimmungsEntscheidung': $(this)[0].value,
                'thesisAbstimmungsId': id,
                'thesisAbstimmungsUser': userId
            })
            poll.setData('/abstimmung/' + id + '/', data, chartData);
        });

        $(document).on('click', '.abstimmung_aendern', function () {
            $('#poll_change').remove();
            $("#poll_content").append(content_card_poll_not_done);
        });
    }
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