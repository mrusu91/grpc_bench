package main

import (
	"log"
	"net"

	"golang.org/x/net/context"
	"google.golang.org/grpc"
	pb "grpc_bench/test"
	"google.golang.org/grpc/reflection"
)

type server struct{}

func (s *server) PostEvent(ctx context.Context, in *pb.Event) (*pb.Event, error) {

	return &pb.Event{
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
  }, nil
}

func main() {
	lis, err := net.Listen("tcp", ":12344")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterEventsServer(s, &server{})
	reflection.Register(s)
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
