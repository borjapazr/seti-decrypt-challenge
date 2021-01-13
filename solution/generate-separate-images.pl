# http://phl.upr.edu/library/notes/SETIChallenge

use strict;
use warnings;
use GD;

my @seti;

my $in = 'SETI_message.txt';
open S, "<$in" or die "Failed to open $in";
while (<S>) {
	push @seti, split(//, $_);
}
close S;

my $cols = 359;
my $rows = 757;
my $images = 7;

for my $i (0..$images-1) {
	my $img = new GD::Image($cols, $rows);
	my $wh = $img->colorAllocate(255, 255, 255);
	my $bl = $img->colorAllocate(0, 0, 0);

	for my $r (0..$rows-1) {
		for my $c (0..$cols-1) {
			my $p = ($seti[$i*$cols*$rows+$c+$r*$cols] eq '0')?$bl:$wh;
			$img->setPixel($c, $r, $p);
		}
	}

	my $out = "images/seti-part-$i.png";
	open P, ">:raw", "$out" or die "Failed to create $out";
	print P $img->png;
	close P;
}