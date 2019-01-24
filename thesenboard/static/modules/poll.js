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
            $('#poll').append(content_card_poll);
            if(poll.isEmpty(data)) $('#poll_content').append(content_card_poll_not_done)
            else $('#poll_content').append(content_card_poll_done)
        }).fail(function () {
            console.log("Request failed...");
        });

    },
    setData: function(path, data, chartData) {
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
        $.get(path, function(returnData) {
            if(jQuery.isEmptyObject(returnData)) {
                 $.ajax({
                    url: path,
                    type: 'PUT',
                    data: data
                  }).done(function() {
                      obj = JSON.parse(data);
                      if(obj.thesisAbstimmungsEntscheidung === 'True') chartData.datasets[0].data[0] = chartData.datasets[0].data[0] + 1;
                      else chartData.datasets[0].data[1] = chartData.datasets[0].data[1] + 1;
                      poll.drawChart(chartData)
                      $('#poll_buttons').fadeOut(300, function() {
                          $(this).remove();
                          $("#poll_content").append(content_card_poll_done);
                      });
                  });
            } else {
                  $.ajax({
                    url: path,
                    type: 'PATCH',
                    data: data
                  }).done(function() {
                      obj = JSON.parse(data);
                      if(obj.thesisAbstimmungsEntscheidung.toString().toLowerCase() !== returnData[0].thesisAbstimmungsEntscheidung.toString().toLowerCase()) {
                          if (obj.thesisAbstimmungsEntscheidung === 'True') {
                              chartData.datasets[0].data[0] = chartData.datasets[0].data[0] + 1;
                              chartData.datasets[0].data[1] = chartData.datasets[0].data[1] - 1;
                          }
                          else {
                              chartData.datasets[0].data[1] = chartData.datasets[0].data[1] + 1;
                              chartData.datasets[0].data[0] = chartData.datasets[0].data[0] - 1;
                          }
                          poll.drawChart(chartData)
                      }
                      $('#poll_buttons').fadeOut(300, function() {
                          $(this).remove();
                          $("#poll_content").append(content_card_poll_done);
                      });
                  });
            }
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