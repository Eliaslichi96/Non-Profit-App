// static/js/index.js

import 'fullcalendar/dist/fullcalendar.css';
import $ from 'jquery';
import 'moment';
import 'fullcalendar';

$(document).ready(function () {
    $('#calendar').fullCalendar({
        events: [
            {
                title: 'Sample Event',
                start: '2021-12-01T10:00:00'
            }
        ]
    });
});
