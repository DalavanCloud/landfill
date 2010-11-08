#!/usr/bin/perl -wT
#
# The contents of this file are subject to the Mozilla Public
# License Version 1.1 (the "License"); you may not use this file
# except in compliance with the License. You may obtain a copy of
# the License at http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS
# IS" basis, WITHOUT WARRANTY OF ANY KIND, either express or
# implied. See the License for the specific language governing
# rights and limitations under the License.
#
# The Original Code is the Landfill Tools System.
#
# The Initial Developer of the Original Code is Everything Solved, Inc.
# Portions created by the Initial Developers are Copyright (C) 2010 the
# Initial Developer. All Rights Reserved.
#
# Contributor(s):
#   Max Kanat-Alexander <mkanat@bugzilla.org>

use strict;
use lib qw(.);
use Landfill;

my $cgi = Landfill->cgi;
my $template = Landfill->template;

print $cgi->header;
$template->process('index.html.tmpl') or die $template->error;
