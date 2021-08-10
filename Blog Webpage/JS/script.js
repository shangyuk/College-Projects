// When the user scrolls the page, execute stick() function
window.onscroll = function() {stick()};

// Get the navigation bar
var nav = document.getElementById("nav");

// Get the offset position the navigation bar
var sticky = nav.offsetTop;

// Add the sticky class to the navigation bar when scroll position is reached. Remove sticky class when the scroll position is left
function stick() 
{
	if (window.pageYOffset >= sticky) 
	{
		nav.classList.add("sticky")
	} else {
		nav.classList.remove("sticky");
	}
}