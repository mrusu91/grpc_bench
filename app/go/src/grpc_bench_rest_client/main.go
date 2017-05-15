package main

import (
  "log"
  "time"

  "grpc_bench_rest_client/client/events"
  "grpc_bench_rest_client/models"

  apiclient "grpc_bench_rest_client/client"
)

func average(input []int64) float64 {
	total := float64(0)
	for _, v := range input {
		total += float64(v)
	}
	return total / float64(len(input))
}

func call() {
  event := models.Event{
    ID:             func(i int32) *int32 { return &i }(1),
    Sport:          func(i string) *string { return &i }("football"),
    Category:       func(i string) *string { return &i }("England"),
    Tournament:     func(i string) *string { return &i }("Premier League"),
    Round:          func(i string) *string { return &i }("32"),
    TeamA:          func(i string) *string { return &i }("Chelsea FC"),
    TeamB:          func(i string) *string { return &i }("Liverpool FC"),
    Score:          func(i string) *string { return &i }("0 - 0"),
    State:          func(i string) *string { return &i }("playing"),
    StartTimestamp: func(i float64) *float64 { return &i }(0.1),
  }
  params := events.NewPostEventsParams()
  params.SetEvent(&event)
  _, err := apiclient.Default.Events.PostEvents(params)
  if err != nil {
    log.Fatal(err)
  }
}

func main() {
  total_start := time.Now()

  durations := make([]int64, 500000)
  for i := 1; i <= 500000; i++ {
    call_start := time.Now()
    call()
    call_elapsed := time.Since(call_start)
    durations = append(durations, call_elapsed.Nanoseconds())
  }
  total_elapsed := time.Since(total_start)
  log.Printf("Total %s", total_elapsed)
  avg := average(durations)
  log.Printf("Avg %s", avg)
}
