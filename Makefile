GENERATED_RPC=./rpc/generated
PROTOS_RPC=./rpc/protos

gp:
	python -m grpc_tools.protoc -I${PROTOS_RPC} --python_out=${GENERATED_RPC} --grpc_python_out=${GENERATED_RPC} ${PROTOS_RPC}/*.proto	
