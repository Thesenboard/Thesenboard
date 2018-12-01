var poll = {
    getData: function (path) {
        var csrftoken = poll.getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!poll.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            contentType: 'application/json',
            processData: false
        });
        $.get(path, function(data) {
            if(poll.isEmpty(data)) $('#poll').append(content_card_poll)
        }).fail(function () {
            console.log("Request failed...");
        });

    },
    setData: function(path, data) {
        var csrftoken = poll.getCookie('csrftoken');
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!poll.csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            contentType: 'application/json',
            processData: false
        });
        $.ajax({
            url: path,
            type: 'PUT',
            data: data
          }).done(function() {
              $('#poll').fadeOut(300, function() {
                  $(this).remove();
              });
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
    isEmpty: function(obj) {
        for(var key in obj) {
            if(obj.hasOwnProperty(key))
                return false;
        }
        return true;
    },
    drawChart: function(data) {
        var ctx = document.getElementById('pollChart').getContext('2d');
        pieChart = new Chart(ctx,{
        type: 'doughnut',
        data: data,
        options: {}
        });
    }
}