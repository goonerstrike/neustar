#!/usr/bin/python
# Script to update CNAME record using ultradns api
# Please refer to https://github.com/ultradns/python_rest_api_client for module

import ultra_test_client
import sys
import optparse

domain = 'restapi.ultradns.com'

parser = optparse.OptionParser()
parser.add_option('-u', dest="username")
parser.add_option('-p', dest="password")
parser.add_option('-d', dest="domain_name")
parser.add_option('-o', dest="old_cname_record")
parser.add_option('-n', dest="new_cname_record")
options, remainder = parser.parse_args()

if options.domain_name or options.old_cname_record or options.new_cname_record or options.username or options.password== None:
        print "Usage: -u <useranme> -p password -d domain -o old_cname_record -n new_cname_record"
        sys.exit()

q = ultra_rest_client.RestApiClient(username, password, 'True' == use_http, domain)
q.edit_rrset(domain_name, "CNAME", old_cname_record, 100, ["options.new_cname_record."])
