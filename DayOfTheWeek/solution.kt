class Solution {
    fun dayOfTheWeek(day: Int, month: Int, year: Int): String {
        val inputDate = java.util.Calendar.getInstance()
        inputDate[year, month - 1] = day
        val weekdays =
            listOf("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
        println(weekdays[inputDate.get(java.util.Calendar.DAY_OF_WEEK) - 1])
        return weekdays[inputDate.get(java.util.Calendar.DAY_OF_WEEK) - 1]
    }
}