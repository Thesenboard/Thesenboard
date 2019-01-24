var InfiniteScroll = {
    getData: function(path, content_card, fields) {
        var csrftoken = InfiniteScroll.getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!InfiniteScroll.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            contentType : 'application/json',
            processData : false
        });
        $.get(path, function( data ) {
          if(data !== 'undefined') {
              var cards = '';
              var dataArray = [];
              if(typeof data.results !== 'undefined') dataArray = data.results;
              else dataArray = data;
              for(var i=0; i<dataArray.length;i++) {
                  var cardData = dataArray[i];
                  var discussionDate = InfiniteScroll.formatDate(cardData[fields.time]);
                  var today = Date.now();
                  var startday = new Date(cardData.thesenTime)
                  var timediff = ((today - startday) / 1000) / (60*60*24);
                  var status = '';
                  if(timediff > 90) status = 'inaktiv';
                  else status = 'aktiv';
                  var replacements = InfiniteScroll.prepareReplacement(cardData);
                  replacements['%status%'] = status;
                  replacements['%datum%'] = discussionDate;
                  if(cardData['thesisEntriesQuelle'] == '') {
                      replacements['%thesisEntriesQuelle%'] = ' ';
                  }
                  cards += InfiniteScroll.replaceAll(content_card, replacements);
              }
              $('#thesen').append(cards);
          } else {
              console.log("keine Daten verfügbar!");
          }
        }).fail(function() {
            console.log("Request failed...");
        });

    },
    getCookie: function(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },
    csrfSafeMethod: function(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    },
    replaceAll: function(card, replacements) {
        card = card.replace(/%\w+%/g, function(all) {
           return replacements[all] || all;
        });
        return card;
    },
    formatDate: function(dateTimeString) {
        var date = new Date(dateTimeString);
        var month = new Array();
        month[0] = 'Januar';
        month[1] = 'Februar';
        month[2] = 'März';
        month[3] = 'April';
        month[4] = 'Mai';
        month[5] = 'Juni';
        month[6] = 'Juli';
        month[7] = 'August';
        month[8] = 'September';
        month[9] = 'Oktober';
        month[10] = 'November';
        month[11] = 'Dezember';
        return date.getDate() + '.' + month[date.getMonth()] + ' ' + date.getFullYear();
    },
    prepareReplacement: function(data) {
        var elements = {};
        for(var key in data) {
            elements['%'+key+'%'] = data[key];
        }
       return elements;
    }
}