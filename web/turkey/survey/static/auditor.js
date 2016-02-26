var submit_auditor;

var total_task_time = 0;
var before_typing_delay = 0;
var on_focus_time = 0; // total - off focus time *********
var within_typing_delay = false; //
var recorded_time_disparity = 0; // total - off focus time **********
var clicks_total = 0;
var clicks_specific = [];		// specific positions and (hopefully) elements clicked inside of
var keypresses_total = 0;
var keypresses_specific = []; 	// There are fields total tabs, total
                            // backspaces, and count of unique characters
                  			// in the paper above, but these can
                            // be extracted from aggregations on
                            // keypresses_specific
var mouse_movement_total = 0;
var mouse_movement_specific = [];
var pastes_total = 0;
var pastes_specific = [];
var scrolled_vertical_pixels_total = 0; // total of position changes via scroll (absolute values)
var scrolled_horizontal_pixels_total = 0;
var scrolled_vertical_pixels_specific = [];        // breakdown of specific_scrolled_pixels in time intervals; actual position, amount in scroll change, or both?
var scrolled_horizontal_pixels_specific = [];
var focus_changes = []; // timestamped


$(document).ready(function() {
// timer start
var timeStart = (new Date()).getTime();

// typing delays; reports FIRST alphabetical typing event
var typing_delay = 10, report_delay = true; // delay is in SECONDS
var report_typing_delay = function() {
	report_delay = false;
	var time = (new Date()).getTime();
	var timestamp = (time - timeStart) / 1000.0;
	if(timestamp < typing_delay) 
		within_typing_delay = true;			
	before_typing_delay = timestamp;
};

// Set the name of the hidden property and the change event for visibility
var hidden, visibilityChange; 
if (typeof document.hidden !== "undefined") { // Opera 12.10 and Firefox 18 and later support 
	hidden = "hidden";
	visibilityChange = "visibilitychange";
} else if (typeof document.mozHidden !== "undefined") {
	hidden = "mozHidden";
	visibilityChange = "mozvisibilitychange";
} else if (typeof document.msHidden !== "undefined") {
	hidden = "msHidden";
	visibilityChange = "msvisibilitychange";
} else if (typeof document.webkitHidden !== "undefined") {
	hidden = "webkitHidden";
	visibilityChange = "webkitvisibilitychange";
}

var off_focus_time = 0, last_focus_time = (new Date()).getTime();
function handleVisibilityChange() {
	var focus_change_time;
	if (document[hidden]) {
	    focus_change_time = (new Date()).getTime();
	    focus_changes.push((focus_change_time - timeStart) / 1000.0);
	    last_focus_time = (new Date()).getTime();
	    // console.log("out of focus: " + (focus_change_time - timeStart) / 1000.0);
	} else {
	    focus_change_time = (new Date()).getTime();
	    off_focus_time += (focus_change_time - last_focus_time) / 1000.0;
	    // console.log("IN FOCUS: " + (focus_change_time - timeStart) / 1000.0);
	    // console.log("total off focus time: " + off_focus_time);
	}
}
document.addEventListener(visibilityChange, handleVisibilityChange, false);

// clicking events
$('*').click(function(e) {
	e.stopPropagation();
	clicks_total += 1;
	clicks_specific.push(this);
	// console.log("clicks: " + clicks_total);
	// console.log(clicks_specific);
}),

// keypress events
$('*').keyup(function(e) {
	e.stopPropagation();

	if(report_delay && 65 <= e.keyCode && e.keyCode <= 90) // key is alphabetical
		report_typing_delay();

	keypresses_total += 1;
	keypresses_specific.push(String.fromCharCode(e.keyCode));
	// console.log("kp: " + keypresses_total);
	// console.log(keypresses_specific);
}),

// paste events
$("input").bind("paste", function(e) {
    e.stopPropagation();
    pastes_total += 1;
	var pasted_data = e.originalEvent.clipboardData.getData('text');
    pastes_specific.push(pasted_data)
    
    // console.log(pasted_data);
}),

// mouse events
$("*").mousemove(function(e) {
    mouse_movement_total += 1;
    var position = [e.pageX, e.pageY];
    mouse_movement_specific.push(position);

    // console.log("mouse move: " + position);
});

// vertical scroll events
var previousV = 0;
$(window).scroll(function() {
	var curr = $(window).scrollTop();
	var timestamp = ((new Date()).getTime() - timeStart) / 1000.0;

	var rawAmount = curr - previousV; // directed scrolling vs total scrolling
	var amount = Math.abs(rawAmount);
	previousV = curr; // update most recent position
	
	scrolled_vertical_pixels_total += amount;
	scrolled_vertical_pixels_specific.push({ 'timestamp' : timestamp, 'position' : curr, 'change' : rawAmount});
	
	//console.log('vertical scroll amount: ' + amount);
	//console.log('vertical scroll total: ' + scrolled_vertical_pixels_total);
});

// horizontal scroll events
var previousH = 0;
$(window).scroll(function() {
	var curr = $(window).scrollTop();
	var timestamp = ((new Date()).getTime() - timeStart) / 1000.0;
	
	var rawAmount = curr - previousH; // directed scrolling vs total scrolling
	var amount = Math.abs(rawAmount);
	previousH = curr; // update most recent position
	
	scrolled_horizontal_pixels_total += amount;
	scrolled_horizontal_pixels_specific.push({ 'timestamp' : timestamp, 'position' : curr, 'change' : rawAmount});

	//console.log('horizontal scroll amount: ' + amount);
	//console.log('horizontal scroll total: ' + scrolled_horizontal_pixels_total);
});

// submit
submit_auditor = function() {
	total_task_time = ((new Date()).getTime() - timeStart) / 1000.0; //seconds
	recorded_time_disparity = total_task_time - off_focus_time;
	on_focus_time = total_task_time - off_focus_time;
	
	return {
		'total_task_time' 						:	total_task_time,
		'before_typing_delay'					:	before_typing_delay,
		'on_focus_time'	 						:	on_focus_time,
		'within_typing_delay' 					: 	within_typing_delay,
		'recorded_time_disparity' 				:	recorded_time_disparity,
		'clicks_total' 							:	clicks_total,
		'clicks_specific' 						:	clicks_specific,
		'keypresses_total' 						: 	keypresses_total,
		'keypresses_specific'					: 	keypresses_specific,
		'mouse_movement_total' 					: 	mouse_movement_total,
		'mouse_movement_specific' 				:	mouse_movement_specific,
		'pastes_total' 							:	pastes_total,
		'pastes_specific'						:	pastes_specific,
		'scrolled_vertical_pixels_total' 		:	scrolled_vertical_pixels_total,
		'scrolled_horizontal_pixels_total'		:	scrolled_horizontal_pixels_total,
		'scrolled_vertical_pixels_specific'		:	scrolled_vertical_pixels_specific,
		'scrolled_horizontal_pixels_specific'	:	scrolled_horizontal_pixels_specific
	};
}

});