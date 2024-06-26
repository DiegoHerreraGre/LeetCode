function dayOfTheWeek(day, month, year) {
	const inputDate = new Date(year, month - 1, day);
	const weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
	console.log(weekdays[inputDate.getDay()])
	return weekdays[inputDate.getDay()];
}

// TEST 1
dayOfTheWeek(5, 1, 1994);