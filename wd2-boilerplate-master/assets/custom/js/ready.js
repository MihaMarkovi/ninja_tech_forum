    $(document).ready(function() {
        var TopicButton = $("#topic-button");
        var TopicSum = $("#sumNumbers");
        TopicButton.click(function(e) {
            if (TopicSum.val() === "10"){
                TopicButton.hide();
            } else {
                alert("You entered a wrong sum! Try again.");
                e.preventDefault();
            }
        });
    });
