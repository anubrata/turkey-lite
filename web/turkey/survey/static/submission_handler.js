var God = {
    steps: [],
        register: function(f) {
        this.steps.push(f);
    }
    on_submit: function() {
    var submission_map = {};
    $.each(this.steps, function(e) {
        var result = e();
        submission[result[0]] = result[1];
    });
    // post submission map to endpoint
    }
}