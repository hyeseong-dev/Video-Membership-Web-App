delimiter //
create trigger channel_sync
after update on c_server
for each row
begin
declare result int;
set result = (select sys_exec("curl -v http://192.168.20.124:55532/monitor/channel-sync"));
end; 