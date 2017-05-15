package main

import (
	"log"
  "time"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "grpc_bench/test"
)

func call(c pb.EventsClient) {
	r, err := c.PostEvent(context.Background(), &pb.Event{
    Id:             1,
    Sport:          "football",
    Category:       "England",
    Tournament:     "Premier League",
    Round:          "32",
    TeamA:          "Chelsea FC",
    TeamB:          "Liverpool FC",
    Score:          "0 - 0",
    State:          "playing",
    StartTimestamp: 0.1,
  })
	if err != nil {
		log.Fatalf("could not post event: %v", err)
	}
	log.Printf("RECV: %v", r)
}

func average(input []int64) float64 {
	total := float64(0)
	for _, v := range input {
		total += float64(v)
	}
	return total / float64(len(input))
}

func main() {
  total_start := time.Now()

  conn, err := grpc.Dial("10.2.1.32:12344", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	c := pb.NewEventsClient(conn)

  durations := make([]int64, 500000)
  for i := 1; i <= 500000; i++ {
    call_start := time.Now()
    call(c)
    call_elapsed := time.Since(call_start)
    durations = append(durations, call_elapsed.Nanoseconds())
  }
  total_elapsed := time.Since(total_start)
  log.Printf("Total %s", total_elapsed)
  avg := average(durations)
  log.Printf("Avg %s", avg)
}
