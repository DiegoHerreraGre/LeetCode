<?php

function dayOfTheWeek($day, $month, $year)
{
	$inputDate = mktime(0, 0, 0, $month, $day, $year);
	$weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
	echo $weekdays[date('w', $inputDate)];
	return $weekdays[date('w', $inputDate)];
}