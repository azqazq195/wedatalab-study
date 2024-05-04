package org.example.week1_dp.돌_게임

import java.io.ByteArrayInputStream
import java.util.*

fun main() {
    val testInput = "5"
    System.setIn(ByteArrayInputStream(testInput.toByteArray()))

    val reader = System.`in`.bufferedReader()
    val st = StringTokenizer(reader.readLine())
    val n = st.nextToken().toInt()

    if (n % 2 == 0)
        println("CY")
    else
        println("SK")
}