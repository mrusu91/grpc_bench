#	python -m grpc_tools.protoc \

fetch_go_deps:
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
	go get -u github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger
	go get -u github.com/golang/protobuf/protoc-gen-go


gen_py_grpc: fetch_go_deps
	python -m grpc_tools.protoc \
		-Iprotos \
		-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--python_out=py/ \
		--grpc_python_out=py/ \
		protos/*
	python -m grpc_tools.protoc \
		-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--python_out=/usr/local/lib/python2.7/dist-packages/ \
		--grpc_python_out=/usr/local/lib/python2.7/dist-packages/ \
		$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/google/api/annotations.proto
	python -m grpc_tools.protoc \
		-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--python_out=/usr/local/lib/python2.7/dist-packages/ \
		--grpc_python_out=/usr/local/lib/python2.7/dist-packages/ \
		$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis/google/api/http.proto
	touch /usr/local/lib/python2.7/dist-packages/google/__init__.py
	touch /usr/local/lib/python2.7/dist-packages/google/api/__init__.py

gen_go_grpc: fetch_go_deps
	protoc \
		-I/protoc3/include \
		-Iprotos \
		-I$(GOPATH)/src \
		-I$(GOPATH)/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
		--go_out=plugins=grpc:go/src/grpc_bench/test \
		--grpc-gateway_out=logtostderr=true:go/src/grpc_bench/test \
		--swagger_out=logtostderr=true:swagger \
		protos/*
	cd go/src/grpc_bench; go get .; cd -;
	cd go/src/grpc_bench_server; go get .; cd -;
	cd go/src/grpc_bench_client; go get .; cd -;

run_py_rest_simple_server:
	gunicorn -b 0.0.0.0:12345 -w 8 -k eventlet 'py.rest_server:simple_app()'

run_py_rest_connexion_server:
	gunicorn -b 0.0.0.0:12345 -w 8 -k eventlet 'py.rest_server:connexion_app()'

run_py_rest_connexion_validation_server:
	gunicorn -b 0.0.0.0:12345 -w 8 -k eventlet 'py.rest_server:connexion_validation_app()'
