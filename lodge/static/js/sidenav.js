var $search = $('#searchIcon'),
    $input   = $('#search_input'),
    visible = false,
    $nav = $('nav ul');
    $side = $('#mySidenav');
    $open = $('#open');
    $close = $('#close');

 $('#search_input').hide();

$search.hover(
	function(){
		console.log("ive been hovered");
		if (visible) {
			console.log("im true!");
			$input.on("focus", function(){
				console.log("im a focus");
			}).mouseleave(function(){
				$(this).fadeOut('slow', function(){
					console.log("im a mouseout");
				});
			});
			visible = false;
		} else {
			console.log("helloooo it's false");
			$input.show(300, function(){
				$(this).addClass('input_style');
				console.log('whattttt', $(this));
				console.log("complete");
			});
			console.log("we skipped stuff");
			visible = true;
		}
});

$open.click(
	function openNav() {
		console.log("whats up");
		$side.css("width", "250px");
	}
);

$close.click(
	function closeNav(){
		console.log("whats up bra");
		$side.css("width", "0");
	});






