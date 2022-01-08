create trigger channel_sync3
AFTER update on c_server
for each row
begin
declare result int;
declare rest int;
declare grpc int;
declare grpc_stream int;
declare body varchar(255);
set rest := new.ch_rest;
set grpc := new.ch_grpc;
set grpc_stream := new.ch_stream;
if new.name<>old.name or new.hostname<>old.hostname or new.role <> old.role or new.ipaddr <> old.ipaddr or new.status <> old.status or new.ch_rest<>old.ch_rest or new.ch_grpc<>old.ch_grpc or new.ch_stream <> old.ch_stream then
set body := concat('{',"rest", ':', rest, ',', 'grpc',':', grpc, ',', 'grpc_stream'':', grpc_stream, '}');
set result = (select sys_exec(concat('curl -v -X POST http://192.168.20.124:55532/monitor/channel-sync -H Content-Type: application/json -d ', body)));
end if; 
end; //