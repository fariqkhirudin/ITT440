#include <stdio.h>

#include <assert.h>

#include <dispatch/dispatch.h>

#include <dns_sd.h>



void callback(DNSServiceRef sdRef,

   DNSServiceFlags flags,

   uint32_t interfaceIndex,

   DNSServiceErrorType errorCode,

   const char *serviceName,

   const char *regtype,

   const char *replyDomain,

   void *context) {



    printf("result: %s %s %s\n", serviceName, regtype, replyDomain);

}



int main(int argc, char const *argv[])

{

    DNSServiceRef client;

    DNSServiceErrorType err;



    err = DNSServiceBrowse(

       &client,

       0,

       0,

       "_raop._tcp.",

       "local.",

       callback,

       NULL

    );

    assert(err == 0);



    DNSServiceSetDispatchQueue(client, dispatch_get_main_queue());

    dispatch_main();



    printf("ok\n");

    return 0;

}

