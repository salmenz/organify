var selected_date = '';
$(document).ready(function () {
    $('.today-date').text($.datepicker.formatDate('dd-M-yy', new Date()));

    $( "#date-picker" ).datepicker({
        dateFormat: 'dd-M-yy',
        onSelect: function(selected) {
            selected_date = selected;
            $('.selected-date').text(selected_date);
            showCreateEvents();
        }});

    $('#add-event').click(function () {
        var $event_name_selector = $('#event-name');
        var event_name = $event_name_selector.val();
        var $event_description_selector = $('#event-description');
        var event_description = $event_description_selector.val();

        if(selected_date.length === 0) {
            alert('Please select a date and continue');
            return false;
        }

        if(event_name.length === 0 || event_description.length === 0 ) {
            alert('Event Name & Description should be present!');
            return false;
        }

        var existing_events = JSON.parse(localStorage.getItem(selected_date));
        var event_data = {'event_name': event_name, 'event_description': event_description};

        if(existing_events) {
            existing_events.push(event_data);
            localStorage.setItem(selected_date, JSON.stringify(existing_events));
        } else {
            localStorage.setItem(selected_date, JSON.stringify([event_data]));
        }

        $event_name_selector.val('');
        $event_description_selector.val('')
        showCreateEvents();
    })
});

function showCreateEvents() {
    var events = JSON.parse(localStorage.getItem(selected_date));
    var $list_events = $('.list-events');

    $list_events.empty();

    if(events) {
        var event_lists = '';

        $.each(events, function (index, event) {
            event_lists += "<span class='index-num'>"+(index+1)+". </span>"+"<span class='event-name'>"+event.event_name+"</span>"+" <span class='event-description'>"+event.event_description+"</span><div></div>"
        });

        $list_events.append(event_lists);
    }
}
