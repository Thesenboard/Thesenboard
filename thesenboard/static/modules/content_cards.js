var content_card_home = '<div class="card home-card"><div class="card-body">'
    + '<div class="row"><div class="col-1"><div class="card-circle">T</div></div>'
    + '<div class="col-10"><div class="home-card-title row">%thesenTitel%</div><div class="home-card-info row">veröffentlicht am %datum%, die Diskussion ist im Status %status%</div></div></div>'
    + '<p class="card-text">%thesenFazit%</p><a href="thesis/%thesenId%/" class="card-link float-right"><button class="btn btn-outline-secondary">Zur Diskussion</button></a></div></div>';

var content_card_discussion = '<div class="card home-card"><div class="card-body">'
    + '<div class="row"><div class="col-1"><div class="card-circle">T</div></div>'
    + '<div class="col-10"><div class="home-card-title row">%thesisEntriesTitel%</div><div class="home-card-info row">veröffentlicht am %datum%, von %thesisEntriesUserId%</div></div></div>'
    + '<p class="card-text">%thesisEntriesArgument%</p>'
    + '<p class="card-text">%thesisEntriesFazit%</p>'
    + '<p class="card-text">%thesisEntriesQuelle%</p>'
    + '</div></div>';

var content_card_poll = '<div class="card home-card"><div class="card-body" id="poll_content">'
    + '</div></div>';

var content_card_poll_not_done =  '<div id="poll_buttons">'
    + '<div class="row"><div class="col-6"><button type="button" name="abstimmung" value="True" class="btn btn-block btn-success abstimmung">Stimme zu</button></div>'
    + '<div class="col-6"><button type="button" name="abstimmung" value="False" class="btn btn-block btn-danger abstimmung">Stimme nicht zu</button></div></div>'
    + '</div>';

var content_card_poll_done = '<div id="poll_change">'
    + '<div class="row"><div class="col-12"><button type="button" name="abstimmung_aendern" value="False" class="btn btn-block btn-danger abstimmung_aendern">Abstimmung ändern</button></div>'
    + '</div>';